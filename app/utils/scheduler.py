from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from services.schedule_service import process_scheduled_emails

scheduler = AsyncIOScheduler(
    timezone="America/Santo_Domingo"
)


scheduler.add_job(
    process_scheduled_emails,
    DateTrigger(run_date=datetime.now())
)


scheduler.add_job(
    process_scheduled_emails,
    CronTrigger(hour=9, minute=0)
)
