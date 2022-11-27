# FastAPI Prisma Test

A repository trying to add Prisma into FastAPI app

## Tech Stack

**API Server:** [FastAPI](https://github.com/tiangolo/fastapi)

**Database ORM:** [Prisma](https://github.com/RobertCraigie/prisma-client-py)

**Dependency Manager:** [PDM](https://github.com/pdm-project/pdm)

## Run Locally

Clone the project

```bash
git clone https://github.com/alan910127/fastapi-prisma-test.git
```

Go to the project directory

```bash
cd fastapi-prisma-test
```

Install dependencies

```bash
pdm install
```

Start the server

```bash
pdm run dev
```

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file

(or instead copy the `.env.example` into `.env`)

`DATABASE_URL`

- If you want to use a database other than SQLite, you should also change the `provider` in `prisma/schema.prisma`

## Prisma

### `prisma migrate dev`

Create a migration script in `dev` environment

### `prisma db push`

Push the migration into database and generate the client (for type definitions)

### `prisma generate`

Generate prisma client without modifying database

> You can also add `--watch` command line option to automatically re-generate the client when there are changes in `prisma/schema.prisma`

### Prisma Studio

Prisma Studio does not work natively with Prisma Client Python

There are two other possible ways to use Prisma Studio:

1. **Download the Prisma Studio app**

   Prisma Studio can be downloaded from: https://github.com/prisma/studio/releases

2. **Use the Node based Prisma CLI**

   If you have Node / NPX installed you can launch Prisma Studio by running the command: `npx prisma studio`

## Editor Support

Turn on string suggestion / completion feature on your code editor to get full power of the type-safe Prisma ORM

### Visual Studio Code

```json
// settings.json
{
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  }
}
```
