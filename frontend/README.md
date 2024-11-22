# RoadWatch frontend
```
Vue.js - The Progressive JavaScript Framework

✔ Project name: … frontend
✔ Target directory "frontend" is not empty. Remove existing files and continue? … No / **Yes**
✔ Add TypeScript? … No / **Yes**
✔ Add JSX Support? … **No** / Yes
✔ Add Vue Router for Single Page Application development? … No / **Yes**
✔ Add Pinia for state management? … No / **Yes**
✔ Add Vitest for Unit Testing? … No / **Yes**
✔ Add an End-to-End Testing Solution? › Cypress
✔ Add ESLint for code quality? … No / **Yes**
✔ Add Prettier for code formatting? … No / **Yes**
✔ Add Vue DevTools 7 extension for debugging? (experimental) … No / **Yes**
```

## Aanbevolen IDE Setup

VSCode of WebStorm + Volar (en schakel Vetur uit).

## Type Ondersteuning voor `.vue` Imports in TS

TypeScript kan standaard geen type-informatie voor `.vue` imports verwerken, dus vervangen we de `tsc` CLI door `vue-tsc` voor type-checking. In editors hebben we [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) nodig om de TypeScript-taalservice bewust te maken van `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint with [ESLint](https://eslint.org/)