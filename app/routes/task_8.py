from fastapi import APIRouter, Response

router = APIRouter(tags=["Стажировка"])

"""
Задание_8. Декоратор - счётчик запросов.

Напишите декоратор который будет считать кол-во запросов сделанных к приложению.
Оберните роут new_request() этим декоратором.
Подумать, как хранить переменную с кол-вом сделаных запросов.
"""
def count_requests():
    async def count_clicks():
       
        try:
            with open('./files/count_requests.txt', 'r') as f:
                s = f.read()
        except FileNotFoundError:
            with open('./files/count_requests.txt', 'w') as f:
                s = '0'
                f.write(s)
        with open('./files/count_requests.txt', 'w') as f:
            if s:
                counts = int(s)
                counts += 1
                f.write(str(counts))
            else:
                counts = 0
                f.write(str(counts))
                
        return await func()
    
    return count_clicks


@router.get("/new_request", description="Задание_8. Декоратор - счётчик запросов.")
async def new_request():
    """Возвращает кол-во сделанных запросов."""

    with open('./files/count_requests.txt', 'r') as f:
            counts = int(f.read())

    cont = f'counts = {counts}'

    return Response(content=cont, status_code=200)
