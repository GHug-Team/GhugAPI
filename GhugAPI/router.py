from rest_framework import routers
from users.urls import router as usersrouter
from news.urls import router as newsrouter
from reminders.urls import router as remindersrouter
from baby.urls import router as babyrouter

router = routers.DefaultRouter()

router.registry.extend(usersrouter.registry)
router.registry.extend(newsrouter.registry)
router.registry.extend(remindersrouter.registry)
router.registry.extend(babyrouter.registry)