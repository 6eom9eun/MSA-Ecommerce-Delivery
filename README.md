<h2>MSA 기반 전자상거래 플랫폼</h2>

<h3>[ Django, Flask ] + RabbitMQ, MySQL : MSA</h3>

![스크린샷 2024-03-10 10 52 20](https://github.com/6eom9eun/MSA_shopDeliver/assets/104510730/b6dde1ef-6cda-40be-8bcf-594d9d78ffc2)

- Languege : Python
- Framework : Django, Flask
- DB : MySQL
- Technology & Tools : Docker(docker-compose), RabbitMQ( [cloudamqp](https://www.cloudamqp.com/) : Little Lemur)<br>


- ### images<br>
  ![스크린샷 2024-03-09 22 58 26](https://github.com/6eom9eun/msaStudy/assets/104510730/9bd79e44-8d34-4f86-9f5b-549d4039cfa7)

- ### Containers<br>
  - docker-compose를 통해 도커라이징
      - order(Django+MySQL+Producer/Consumer)
      - boss(Flask+MySQL+Porducer/Consumer)
        
        <img width="641" alt="스크린샷 2024-03-09 23 00 27" src="https://github.com/6eom9eun/msaStudy/assets/104510730/e250d922-785c-45ea-bd90-898da36da4e1">
  
- ### What ?<br>
  - Django
      - Django 애플리케이션에서는 상점과 주문에 대한 CRUD 작업을 처리합니다.
      - Django 애플리케이션은 RabbitMQ 큐 'order'에 주문에 대한 메시지를 소비합니다.
      - 소비된 메시지는 주문 데이터베이스의 해당 주문을 찾아서 배송 완료 상태를 업데이트합니다.
  - Flask
      - Flask 애플리케이션은 RabbitMQ 큐 'boss'에 상점과 주문에 대한 메시지를 소비합니다.
      - 소비된 메시지는 Flask 애플리케이션의 데이터베이스에 상점 및 주문을 생성, 업데이트 또는 삭제합니다.

- ### API (Django)<br>
  - 가게 리스트 조회 `GET`
    - Endpoint : localhost:8000/api/shop
  - 가게 추가 `POST`
    - Endpoint : localhost:8000/api/shop
  - 특정 가게 조회 `GET`
    - Endpoint : localhost:8000/api/shop/\<id>
  - 특정 가게 수정 `PUT`
    - Endpoint : localhost:8000/api/shop/\<id>
  - 특정 가게 삭제 `DELETE`
    - Endpoint : localhost:8000/api/shop/\<id>
  - 주문 리스트 조회 `GET`
    - Endpoint : localhost:8000/api/order
  - 주문 추가 `POST`
    - Endpoint : localhost:8000/api/order
  - 특정 주문 조회 `GET`
    - Endpoint : localhost:8000/api/order/\<id>
  - 특정 주문 수정 `PUT`
    - Endpoint : localhost:8000/api/order/\<id>
  - 특정 주문 삭제 `DELETE`
    - Endpoint : localhost:8000/api/order/\<id>
- ### API (Flask)<br>
  - 가게 리스트 조회 `GET`
    - Endpoint : localhost:8001/api/shop
  - 특정 가게 조회 `GET`
    - Endpoint : localhost:8001/api/shop/\<id>
  - 특정 주문 배송 완료 처리 `POST`
    - Endpoint : localhost:8001/api/order/\<id>/deliver_finish
- `필드는 코드에서 확인`
