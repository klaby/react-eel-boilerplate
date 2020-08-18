export {}

declare global {
  interface Window {
    eel: {
      hello: () => void
    }
  }
}
