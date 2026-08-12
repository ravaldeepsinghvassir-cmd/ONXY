"""
ONXY Skill Registry

Central registry for discovering, managing,
searching and executing professional skills.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Skill:
    """Represents one ONXY professional skill."""

    name: str
    description: str
    category: str
    version: str = "1.0.0"

    capabilities: List[str] = field(default_factory=list)
    tools: List[str] = field(default_factory=list)

    handler: Optional[Callable[..., Any]] = None

    enabled: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)

    def execute(self, *args, **kwargs) -> Any:
        """Execute the skill."""

        if not self.enabled:
            raise RuntimeError(
                f"Skill '{self.name}' is disabled."
            )

        if self.handler is None:
            raise RuntimeError(
                f"Skill '{self.name}' has no execution handler."
            )

        return self.handler(*args, **kwargs)


class SkillRegistry:
    """Central registry for ONXY skills."""

    def __init__(self) -> None:
        self._skills: Dict[str, Skill] = {}

    def register(self, skill: Skill) -> None:
        """Register a skill."""

        if not isinstance(skill, Skill):
            raise TypeError(
                "Only Skill instances can be registered."
            )

        key = skill.name.strip().lower()

        if not key:
            raise ValueError(
                "Skill name cannot be empty."
            )

        self._skills[key] = skill

    def unregister(self, name: str) -> bool:
        """Remove a skill."""

        key = name.strip().lower()

        if key in self._skills:
            del self._skills[key]
            return True

        return False

    def get(self, name: str) -> Optional[Skill]:
        """Get a skill by name."""

        return self._skills.get(
            name.strip().lower()
        )

    def exists(self, name: str) -> bool:
        """Check whether a skill exists."""

        return (
            name.strip().lower()
            in self._skills
        )

    def list_all(self) -> List[Skill]:
        """Return all registered skills."""

        return list(self._skills.values())

    def list_enabled(self) -> List[Skill]:
        """Return enabled skills."""

        return [
            skill
            for skill in self._skills.values()
            if skill.enabled
        ]

    def by_category(
        self,
        category: str,
    ) -> List[Skill]:
        """Return skills by category."""

        category = category.strip().lower()

        return [
            skill
            for skill in self._skills.values()
            if skill.category.lower() == category
        ]

    def search(self, query: str) -> List[Skill]:
        """Search skills."""

        query = query.strip().lower()

        if not query:
            return self.list_enabled()

        results: List[Skill] = []

        for skill in self.list_enabled():

            searchable = " ".join(
                [
                    skill.name,
                    skill.description,
                    skill.category,
                    *skill.capabilities,
                    *skill.tools,
                ]
            ).lower()

            if query in searchable:
                results.append(skill)

        return results

    def execute(
        self,
        name: str,
        *args,
        **kwargs,
    ) -> Any:
        """Execute a registered skill."""

        skill = self.get(name)

        if skill is None:
            raise KeyError(
                f"Skill '{name}' is not registered."
            )

        return skill.execute(
            *args,
            **kwargs,
        )

    def summary(self) -> Dict[str, Any]:
        """Return registry statistics."""

        skills = self.list_all()

        return {
            "total": len(skills),
            "enabled": sum(
                skill.enabled
                for skill in skills
            ),
            "disabled": sum(
                not skill.enabled
                for skill in skills
            ),
            "categories": sorted(
                {
                    skill.category
                    for skill in skills
                }
            ),
        }