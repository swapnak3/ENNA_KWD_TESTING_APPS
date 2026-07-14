# -*- coding: utf-8 -*-
"""Created on 29.09.2023.

@project: .
@author: SPLATZP: Pascal Platzer.

Contains helper functions for xpath.
"""
import logging
from datetime import timedelta, date

MODULE_LOGGER = logging.getLogger(__name__)


def next_date_by_weekday(weekday) -> date | bool:
	"""Calculate datetime for weekday.

		:param str weekday: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"n.
		:returns: date The calculated datetime.
		:rtype: date | bool.
	"""
	weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	try:
		weekday_index = weekdays.index(weekday)
	except ValueError as e:
		MODULE_LOGGER.error(e)
		return False

	current_date = date.today()
	days_until_desired_days = (weekday_index - current_date.weekday() + 7) % 7
	next_date = current_date + timedelta(days=days_until_desired_days)
	return next_date


def get_date_by_type(day_type) -> date | bool:
	"""Calculate datetime for weekday.

		:param str day_type: "YESTERDAY", "TODAY", "TOMORROW" only.
		:returns: date The calculated datetime.
		:rtype: date | bool.
	"""
	today = date.today()

	if day_type.upper() == "YESTERDAY":
		target_date = today - timedelta(days=1)
	elif day_type.upper() == "TOMORROW":
		target_date = today + timedelta(days=1)
	elif day_type.upper() == "TODAY":
		target_date = today
	else:
		return False

	return target_date
