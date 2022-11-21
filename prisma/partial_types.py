from prisma.models import User

User.create_partial("UserWithoutId", exclude={"id"})
User.create_partial("UserWithoutPassword", exclude={"password"})
