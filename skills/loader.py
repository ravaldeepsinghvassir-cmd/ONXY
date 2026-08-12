"""
ONXY Automatic Skill Loader

Discovers and loads skill modules directly from
the ONXY skills package.
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from typing import List

from .base import BaseSkill
from .registry import Skill, SkillRegistry


class SkillLoader:
    """Automatically discovers ONXY skills."""

    INTERNAL_MODULES = {
        "skills.base",
        "skills.registry",
        "skills.loader",
        "skills.__init__",
    }

    def __init__(self, registry: SkillRegistry) -> None:
        self.registry = registry
        self.loaded_modules: List[str] = []
        self.errors: List[str] = []

    def discover(self) -> List[str]:
        """Discover skill modules inside skills/."""

        package = importlib.import_module("skills")

        discovered: List[str] = []

        for module_info in pkgutil.iter_modules(
            package.__path__
        ):
            module_name = f"skills.{module_info.name}"

            if module_name in self.INTERNAL_MODULES:
                continue

            if module_info.ispkg:
                continue

            discovered.append(module_name)

        return discovered

    def load_module(self, module_name: str) -> int:
        """Load one skill module."""

        registered = 0

        try:
            module = importlib.import_module(module_name)

            for _, obj in inspect.getmembers(
                module,
                inspect.isclass,
            ):
                if obj is BaseSkill:
                    continue

                if not issubclass(obj, BaseSkill):
                    continue

                if inspect.isabstract(obj):
                    continue

                skill_instance = obj()

                skill = Skill(
                    name=skill_instance.name,
                    description=skill_instance.description,
                    category=skill_instance.category,
                    version=skill_instance.version,
                    capabilities=list(
                        skill_instance.capabilities
                    ),
                    tools=list(
                        skill_instance.required_tools
                    ),
                    handler=skill_instance.execute,
                    metadata=skill_instance.metadata(),
                )

                self.registry.register(skill)
                registered += 1

            self.loaded_modules.append(module_name)

        except Exception as exc:
            self.errors.append(
                f"{module_name}: "
                f"{type(exc).__name__}: {exc}"
            )

        return registered

    def load_all(self) -> int:
        """Discover and load all skills."""

        total = 0

        for module_name in self.discover():
            total += self.load_module(module_name)

        return total

    def status(self) -> dict:
        """Return loader status."""

        return {
            "discovered_modules": self.discover(),
            "loaded_modules": list(
                self.loaded_modules
            ),
            "errors": list(self.errors),
            "skills_registered": len(
                self.registry.list_all()
            ),
        }