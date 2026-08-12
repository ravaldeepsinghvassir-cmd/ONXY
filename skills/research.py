"""
ONXY Research Skill

Connects the professional Research Skill
to ONXY's existing web_search action.
"""

from __future__ import annotations

from typing import Any, Dict

from .base import BaseSkill
from actions.web_search import web_search


class ResearchSkill(BaseSkill):
    """
    Professional research capability.

    Uses ONXY's existing web_search action
    instead of duplicating search functionality.
    """

    name = "research"

    description = (
        "Research a topic using ONXY's web search "
        "capabilities and return structured findings."
    )

    category = "research"
    version = "2.0.0"

    capabilities = [
        "topic research",
        "web research",
        "information gathering",
        "source discovery",
        "research summarization",
    ]

    required_tools = [
        "web_search",
    ]

    def execute(
        self,
        input_data: Any,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Execute real web research.
        """

        if not self.validate_input(input_data):
            raise ValueError(
                "Research topic cannot be empty."
            )

        topic = str(input_data).strip()

        if not topic:
            raise ValueError(
                "Research topic cannot be empty."
            )

        try:
            result = web_search(
                query=topic,
                mode="research",
            )

            return {
                "skill": self.name,
                "status": "success",
                "topic": topic,
                "result": result,
            }

        except Exception as exc:
            return {
                "skill": self.name,
                "status": "error",
                "topic": topic,
                "error": str(exc),
            }