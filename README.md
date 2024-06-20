# System zarządzania parkingiem

## Opis
Inteligentny system zarządzania parkingiem, który wykorzystuje AI do przewidywania dostępności miejsc parkingowych. Implementuje dodatkowe funkcjonalności takie jak dodawanie nowych miejsc parkingowych, usuwania miejsc parkingowych, ustawianie statusu zajęcia miejsca i wyświetlanie wszystkich miejsc parkingowych zapisanych w bazie danych.

## Technologie
- Rest API (Flask)
- Bazy danych (SQLite3)
- AI (Scikit-learn)
- Operacje na tablicach (numpy)

## API
- `GET /api/parking_spots`: Zwraca listę wszystkich zapisanych w bazie danych miejsc parkingowych
- `POST /api/add_parking_spot`: Dodaje nowe miejsce parkingowe
- `DELETE /api/remove_parking_spot/<spot_number>`: Usuwa miejsce parkingowe o podanym numerze
- `POST /api/predict_availability`: Przewiduje dostępność miejsc parkingowych na podstawie dnia tygodnia, godziny i informacji czy dany dzień to święto
- `PUT /api/change_occupied`: Aktualizuje informację o tym czy dane miejsce jest aktualnie zajęte

# Baza danych
- `/init_db`: Inicjalizuje bazę danych
- `/fill_db`: Dodaje przykładowe dane do bazy danych

### Przykład danych dla `POST /api/add_parking_spot`
```json
{
    "spot_number": "C13",
    "occupied": false
}
```

### Przykład danych dla `PUT /api/change_occupied`
```json
{
  "spot_number": "A1",
  "occupied": false
}
```

### Przykład danych dla `POST /api/predict_availability`
- Dzień tygodnia opisany przez wartości 0-6 (poniedziałek-niedziela)
- Godzina opisana przez wartości 6-22
- Święta opisane przez wartość 1, a zwykłe dni przez wartość 0
```json
{
    "day_off_week": 3,
    "hour": 6,
    "is_holiday": 0
}
```
