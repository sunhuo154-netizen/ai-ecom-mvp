# AI E-commerce MVP

Full-stack MVP with a FastAPI backend and a Next.js frontend. The app uses mock product and AI data only.

## Project Structure

```text
ai-ecom-mvp/
  backend/
    app/
      api/
        routes/
          ai.py
          products.py
        router.py
      core/
        config.py
      data/
        mock_products.py
      models/
        ai.py
        product.py
      services/
        ai_service.py
        product_service.py
      main.py
    requirements.txt
  frontend/
    app/
      products/
        [id]/
          page.tsx
      globals.css
      layout.tsx
      page.tsx
    components/
      AiGenerator.tsx
      ProductCard.tsx
    lib/
      api.ts
      types.ts
    next.config.js
    package.json
    tsconfig.json
```

## Run Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

