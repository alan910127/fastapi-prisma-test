# FastAPI Prisma Test

## Overview

- Package Manager: [PDM](https://pdm.fming.dev/latest/)
- API Server: [FastAPI](https://fastapi.tiangolo.com)
- Database ORM: [Prisma](https://www.prisma.io)
  - Python Adapter: [Prisma Client Python](https://prisma-client-py.readthedocs.io/en/stable/)
- Authentication: OAuth2 Password Flow

## Development Server

### `pdm run dev`

Starts a development server running locally on http://localhost:8000.

## Prisma

### `pdm run prisma migrate dev`

Create a migration script on `dev` environment.

### `pdm run prisma db push`

Push the migration into database and generate the client (for type definitions).

### `pdm run prisma generate`

Generate prisma client without modifying database.

> Can add `--watch` option to watch the change in `prisma/schema.prisma` and automatically re-generate the client.

### Prisma Studio

Prisma Studio does not work natively with Prisma Client Python

There are two other possible ways to use Prisma Studio:

1. **Download the Prisma Studio app**

   Prisma Studio can be downloaded from: https://github.com/prisma/studio/releases

2. **Use the Node based Prisma CLI**

   If you have Node / NPX installed you can launch Prisma Studio by running the command: `npx prisma studio`

## Editor Support

Turn on string suggestion / completion feature on your code editor to get full benefit from the powerful type-safe Prisma ORM.

### Visual Studio Code

```json
// settings.json
{
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  }
  // ...
}
```
