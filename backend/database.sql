
use guakamayafood;

insert into products (title, price, discount_price, stars, categorie, description, image) 
VALUES  ("Empanada de carne", 2, 1.5, 4, "Desayunos", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Empanada de queso", 10, 2.5, 4, "Almuerzos", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Empanada de pollo", 20, 1.5, 4, "Desayunos", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Arepa con queso", 2.4, 5, 4, "Dulces", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Bollitos de maiz", 2, 4.5, 4, "Desayunos", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Ceviche", 12, 1.5, 1, "Almuerzos", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Tacos", 240, 1.5, 2, "Desayunos", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Mistolín", 2, 1.5, 3.5, "Desayunos", "Empanada sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Cocacola", 2, 1.5, 3.5, "Bebidas", "Cocacola", "http://localhost:8080/static/img/design.png"),
        ("Pepsicola", 2, 1.5, 3.5, "Desayunos", "Coca sabrosa", "http://localhost:8080/static/img/design.png"),
        ("Glup", 2, 1.5, 3.5, "Bebidas", "No sabrosa", "http://localhost:8080/static/img/design.png");


INSERT INTO users (username, first_name, last_name, email, password, country, city, birthday)
VALUES ("jcjohan2707", "Johan Alejandro", "Garcia Castillo", "jcjohan2707@gmail.com", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", "Venezuela", "Caracas", "27/07/2001"),
        ("yoiberth_p", "Yoiberth", "Paredes", "jcjohan27@gmail.com", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", "Venezuela", "Caracas", "27/07/1998"),
        ("compralotodo", "Andrea Johana", "Guerra Castillo", "johan2707@gmail.com", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", "Venezuela", "Caracas", "27/07/2001");


