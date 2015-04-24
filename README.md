# django-search-admin
Поиск в админке по вычисляемому полю

В джанговской админке есть встроенный механизм поиска по полям модели. Достаточно просто указать поле search_fields в классе, унаследованном от ModelAdmin, и поиск по нужным полям заработает сам. Однако, иногда возникают задачи обеспечить поиск не только по простым полям, но и по значениям, сгенерированным методами. Это тоже возможно.
