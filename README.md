<h2>[ Django, Flask ] + RabbitMQ, MySQL : MSA</h2>

![스크린샷 2024-03-10 10 52 20](https://github.com/6eom9eun/MSA_shopDeliver/assets/104510730/b6dde1ef-6cda-40be-8bcf-594d9d78ffc2)

`Languege : Python`<br>
`Framework : Django, Flask`<br>
`DB : MySQL`<br>
`Technology & Tools : Docker(docker-compose), RabbitMQ(cloudamqp : Little Lemur)`

- ### images<br>
  ![스크린샷 2024-03-09 22 58 26](https://github.com/6eom9eun/msaStudy/assets/104510730/9bd79e44-8d34-4f86-9f5b-549d4039cfa7)

- ### Containers<br>
  <img width="641" alt="스크린샷 2024-03-09 23 00 27" src="https://github.com/6eom9eun/msaStudy/assets/104510730/e250d922-785c-45ea-bd90-898da36da4e1">
  
- ### 설명<br>
   - Django로 상점, 주문 CURD -> 메시지 브로커 -> Flask에 상점, 주문 CRUD
   - Flask로 주문 배송 완료 처리 U -> 메시지 브로커 -> Django에 주문 완료 처리 U

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
    - Endpoint : localhost:8001/api/shop/id
  - 특정 주문 배송 완료 처리 `POST`
    - Endpoint : localhost:8001/api/order/\<id>/deliver_finish
- `필드는 코드에서 확인`
