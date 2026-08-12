"""
ONXY Professional Skill Base

Standard interface that every ONXY skill should follow.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseSkill(ABC):
    """
    Base class for all ONXY professional skills.

    Every skill should define:
        - name
        - description
        - category
        - capabilities
        - execute()
    """

    name: str = "unnamed_skill"
    description: str = ""
    category: str = "general"
    version: str = "1.0.0"

    capabilities: List[str] = []
    required_tools: List[str] = []

    def metadata(self) -> Dict[str, Any]:
        """
        Return standardized skill metadata.
        """

        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "version": self.version,
            "capabilities": list(self.capabilities),
            "required_tools": list(
                self.required_tools
            ),
        }

    def validate_input(
        self,
        input_data: Any,
    ) -> bool:
        """
        Basic input validation hook.

        Individual skills can override this.
        """

        return input_data is not None

    def can_execute(
        self,
        input_data: Any,
    ) -> bool:
        """
        Determine whether the skill can handle
        the supplied input.
        """

        return self.validate_input(input_data)

    @abstractmethod
    def execute(
        self,
        input_data: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Execute the skill.

        Every concrete skill must implement this.
        """

        raise NotImplementedError

    def health_check(self) -> Dict[str, Any]:
        """
        Basic health information for the skill.
        """

        return {
            "name": self.name,
            "version": self.version,
            "status": "ready",
        }