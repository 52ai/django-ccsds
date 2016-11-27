import datetime

from django.utils import timezone
from django.test import TestCase


from polls.models import Poll
from django.core.urlresolvers import reverse
# Create your tests here.

class PollMethodTests(TestCase):
	def test_was_published_recently_with_future_Poll(self):
		"""
		was_published_recently() should return False for Poll whose pub_date is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_Poll = Poll(pub_date = time)
		self.assertEqual(future_Poll.was_published_recently(), False)
	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for Poll whose pub_date is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		old_poll = Poll(pub_date=time)
		self.assertEqual(old_poll.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() should return True for Poll whose pub_date is within the last day.
		"""
		time = timezone.now() - datetime.timedelta(days=1)
		old_poll = Poll(pub_date=time)
		self.assertEqual(old_poll.was_published_recently(), True)

