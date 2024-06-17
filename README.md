# Automatyzacja testów API z wykorzystaniem curl

## Opis

Skrypt testuje publiczne API JSONPlaceholder. Wysyła żądania HTTP GET do trzech endpointów i sprawdza poprawność odpowiedzi.

## Uruchomienie skryptu

1. Zainstaluj Python 3.x.
2. Skopiuj skrypt `test_api.py` do lokalnego katalogu.
3. W terminalu uruchom skrypt:
    ```sh
    python test.py
    ```

## Struktura skryptu

- `send_request(url)`: Wysyła żądanie GET przy pomocy `curl`, zwraca odpowiedź w formacie JSON i kod statusu HTTP.
- `check_response(response, key)`: Sprawdza, czy klucz występuje w uzyskanej odpowiedzi.
- `main()`: Funkcja główna, wykonuje test 3 endpointów.

## Wyniki testów

Wyniki testów zostaną wyświetlone w konsoli w formacie:
- `Test 1: PASSED`
- `Test 2: FAILED`

Każdy test sprawdza, czy odpowiedź zawiera kluczowe elementy: `userId`, `id`, `name`.

## Wymagania

- Python 3.x
- curl (zainstalowane w systemie)

## Autor

Kamil Bartosiak
