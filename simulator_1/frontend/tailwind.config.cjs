/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#b3cde0',
          200: '#6497b1',
          300: '#005b96',
          400: '#03396c',
          500: '#011f4b',
        },
        dark: {
          400: '#1d1e23',
          500: '#000000',
        },
        'button-color': '#0097fd',
        'bg-dark': '#1B1E4B',
        'dark-blue': '#2E3A59',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/forms'),
  ],
}
