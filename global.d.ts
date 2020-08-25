export {}

declare global {
  interface Window {
    eel: {
      hello: () => void
      set_host(path: string): void
    }
  }
}
