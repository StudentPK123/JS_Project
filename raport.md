# Projekt z Języków Symbolicznych

### Dawid Szewczyk (GL3)

___

## Temat projektu

Celem projektu jest implementacja sustemu pozwalającego na wyszukiwanie połączeń kolejowych pomiędzy stacjami w języku Python. 
W systemie można tworzyć jak również usuwać połączenia kolejowe pomiędzy poszczególnymi miastami, jak również zaimplementowany 
został algorytm pozwalający na wyszukiwanie najkrótszej drogi pozwalającej na dotarcie z punktu a do punktu b. System wpiera 
również wyszukiwanie tras, które nie posiadają między sobą bezpośrednich połączeń kolejowych.
___
## Funkcjonalność

1. System ma zadeklarowaną listę miast jak również przykładową bazę połączeń
####Pierwsze okno:
* Służy do tworzenia lub usuwania połączeń między poszczególnymi miastami.
* Pozwala wybrać interesującą nas implementację grafu
* Wyświetlenie macierzy połączeń
    * ####Elementy interfejsu użytkownika 
      * Rozwijana lista -> określa punkt startowy
      * Rozwijana lista -> określa punkt docelowy
      * Przycisk "Połącz" -> służy do utworzenia połączenia
      * Przycisk "Rozłącz" -> służy do usunięcia połączenia
      ####
      * Radiobutton pozwalający na wybór danego typu formatowania danych 
        * Macierz sąsiedztwa 
        * Listą sąsiedztwa
      ####
      * Graficzna implementacja połączeń

####Drugie okno:
* Służy do wyświetlania połączeń między wybranymi miastami.
    * ####Elementy interfejsu użytkownika 
      * Rozwijana lista -> określa punkt startowy
      * Rozwijana lista -> określa punkt docelowy
      * Przycisk "Szukaj" -> uruchamia algorytm slużący do wyszukiwania połączeń

___

## Specyfikacja funkcji oraz klas zaimplementowanych do projektu
___

### Klasa [MainWindow](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L23)
Główna klasa programu odpowiedzialna za renderowanie okienek jak również pozwala na wykonywanie podstawowych operacji z poziomu interfejsu użytkownika.

### Funkcja [show_error_message_tk](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L10)
Wyświetlenie okienka z tytułem "Błąd" oraz treścią błędu

### Funkcja [show_showinfo_message_tk](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L14)
Wyświetlenie okienka z tytułem "Sukces" oraz treścią sukcesu

### Funkcja [show_error_message](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L18)
Wyświetlenie okienka z tytułem "Bład" oraz treścią statusu połączenia między miastami w zależności od parametru z jakim została przesłana wiadomość

### Funkcja [on_reload_database](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L104)
Funkcja służąca do wywołania aktualizacji bazy połączeń

### Funkcja [on_update_database_connection](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L109)
Funkcja służąca do ustawienia pozycji polączenia w danym wierszu macierzy.

### Funkcja [update_graph](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L118)
Funkcja służąca do aktualizacji grafu.

### Funkcja [force_update_connections_tree_list](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L125)
Funkcja służąca do aktualizacji/tworzenia bazy połączeń

### Funkcja [find_connection_button_handler](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L137)
Funkcja służąca do znalezienia połączenia pomiędzy dwoma punktami wybranymi przez użytkownika

### Funkcja [manage_connection_button_handler](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/UI/Windows.py#L150)
Funkcja odpowiedzialna za poprawne dodawanie i usuwanie połączeń między dwoma miastami

___

### Moduł Exception

### Klasa [RailwayConnectionErrorType](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/exceptions/Exceptions.py#L3)
Klasa pozwalająca na przekazanie jako parametr odpowiedniego argumentu (1 - istnieje, 2 - nie istnieje) określającego stan połączenia kolejowego

### Klasa [RailwayConnectionError](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/exceptions/Exceptions.py#L16)
Klasa błędu wywoływana w przypadku błędów w połączeniu kolejowym.
* connection -- połączenie, które spowodowało błąd
* error_type -- jaki typ błędu

___

### Klasa [Database](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L35)
Klasa odpowiedzialna za przechowywanie danych jak również zarządzanie nimi oraz callbackami wywołań

### Funkcja [get_city_name_by_id](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L49)
Funkcja odpowiedzialna za pobranie nazwy miasta po id

### Funkcja [add_update_callback](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L52)
Funkcja odpowiedzialna za dodanie callbacku na koniec listy update_callbacks

### Funkcja [add_realod_callback](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L55)
Funkcja odpowiedzialna za dodanie callbacku na koniec listy reload_callbacks

### Funkcja [get_city_id_by_name](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L58)
Funkcja odpowiedzialna za pobranie id miasta po nazwie

### Funkcja [has_connection](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L61)
Funkcja odpowiedzialna za sprawdzenie czy pomiędzy dwoma miastamia jest połączenie

### Funkcja [get_city_list](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L64)
Funkcja odpowiedzialna za pobranie listy miast

### Funkcja [get_connections](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L67)
Funkcja odpowiedzialna za pobranie listy połączeń

### Funkcja [mange_connection](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/database/Database.py#L70)
Funkcja odpowiedzialna za zarządzanie danym połączeniem poprzez dodanie lub usunięcie go z listy (obsługa błędów)

___

### Moduł Graphs

### Klasa [AbstractGraph](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L5)
Nadrzędna klasa abstrakcyjna podstawowe abstrakcyjne metody oraz główną funkcę odpowiedzialną za wyszukiwanie połączeń

### Funkcja [find_connection](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L14)
Funkcja odpowiedzialna za wyszukiwanie połączeń algorytmem BFS

___

### Klasa [AdjacencyLists](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L36)
Klasa operująca na liście sąsiedztwa

### Funkcja [get_nodes](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L44)
Funkcja odpowiedzialna za pobranie węzła po indeksie miasta

### Funkcja [on_update](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L47)
Funkcja odpowiedzialna za dodanie lub usunięcie danego połączenia

### Funkcja [on_reload](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L50)
Funkcja odpowiedzialna za przeładowanie danych

### Funkcja [force_update](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L53)
Funkcja odpowiedzialna za aktualizację danych

### Funkcja [debug_print](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L59)
Funkcja odpowiedzialna za możliwość wypisania danych w konsoli

___

### Klasa [NeighborhoodMatrix](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L64)
Klasa operująca na macierzy sąsiedztw

### Funkcja [on_update](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L73)
Funkcja odpowiedzialna za dodanie lub usunięcie danego połączenia

### Funkcja [on_reload](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L76)
Funkcja odpowiedzialna za przeładowanie danych

### Funkcja [is_connection](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L79)
Funkcja odpowiedzialna za sprawdzenie połączenia

### Funkcja [force_update](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L82)
Funkcja odpowiedzialna za aktualizację danych

### Funkcja [debug_print](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L88)
Funkcja odpowiedzialna za możliwość wypisania danych w konsoli

### Funkcja [get_nodes](https://github.com/StudentPK123/JS_Project/blob/4a93e88664d76bc6dff810882a86c51c312619cf/graphs/Graphs.py#L115)
Funkcja odpowiedzialna za pobranie węzła po indeksie miasta

___

## Moduł Tests

### Klasa [TestRailwayConnections ](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L4)
Klasa odpowiedzialna za wykonanie testów jednostkowych dla poszczególnych sytuacji

### Funkcja [helper_tester_b](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L5)
Funkcja odpowiedzialna za wybór odpowiedniej reprezentacji grafu (test 2, test 6)

### Funkcja [helper_tester_c](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L10)
Funkcja odpowiedzialna za wybór odpowiedniej reprezentacji grafu (test 3, test 7)

### 1 Test [test_connection_between_two_cities](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L19)
Test odpowiedzialny za sprawdzenie poprawnego połączenia między dowma miastami

### 2 Test [test_connections_between_two_cities_with_switches](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L25)
Test odpowiedzialny za sprawdzenie poprawnego połączenia między dwoma miastami z przynajmniej dwoma przesiadkami (AdjacencyLists)

### 3 Test [test_connection_between_two_cities_after_add](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L29)
Test odpowiedzialny za dodanie bezpośredniego połączenia między dwoma miastami i sprawdzenie poprawności wyniki (AdjacencyLists)

### 4 Test [test_connection_between_two_cities_after_remove](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L33)
Test odpowiedzialny za usunięcie bezpośredniego połączenia między miastami i sprawdzenie połączenia z przesiadkami

### 5 Test [test_delete_all_connections](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L42)
Test odpowiedzialny za usunięciu połączeń do danego miasta i sprawdzenie odpowiedniego komunikatu

### 6 Test [test_connections_between_two_cities_with_switches_second_graph](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L55)
Test odpowiedzialny za sprawdzenie poprawnego połączenia między dwoma miastami z przynajmniej dwoma przesiadkami (NeighborhoodMatrix)

### 7 Test [test_connection_between_two_cities_after_add_second_graph](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/test.py#L59)
Test odpowiedzialny za dodanie bezpośredniego połączenia między dwoma miastami i sprawdzenie poprawności wyniki (NeighborhoodMatrix)

___

## Istotne fragmenty kodu

### List/dictionary comprehensions

1. [Link 1](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/graphs/Graphs.py#L129)
1. [Link 2](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/UI/Windows.py#L111)
3. [Link 3](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/graphs/Graphs.py#L69)

### Wyrażenia lambda

1. [Link 1](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/UI/Windows.py#L62)
1. [Link 2](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/UI/Windows.py#L65)
3. [Link 3](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/UI/Windows.py#L70)
3. [Link 4](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/UI/Windows.py#L75)

### Klasy

1. [AbstractGraph / AdjacencyLists / NeighborhoodMatrix](https://github.com/StudentPK123/JS_Project/blob/main/graphs/Graphs.py)
2. [Database](https://github.com/StudentPK123/JS_Project/blob/main/database/Database.py)
3. [RailwayConnectionErrorType / RailwayConnectionError](https://github.com/StudentPK123/JS_Project/blob/main/exceptions/Exceptions.py)
3. [MainWindow](https://github.com/StudentPK123/JS_Project/blob/main/UI/Windows.py)

### Wyjątki

1. [RailwayConnectionError](https://github.com/StudentPK123/JS_Project/blob/058c1b03b371420857a476ce22e2e55f0266e6c3/exceptions/Exceptions.py#L17)

### Moduły

1. [UI](https://github.com/StudentPK123/JS_Project/tree/main/UI)
2. [database](https://github.com/StudentPK123/JS_Project/tree/main/database)
3. [exceptions](https://github.com/StudentPK123/JS_Project/tree/main/exceptions)
3. [graphs](https://github.com/StudentPK123/JS_Project/tree/main/graphs)