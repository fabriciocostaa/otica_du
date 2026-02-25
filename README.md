Recentemente, concluí um projeto: um sistema de registro de pacientes para uma clínica, desenvolvido do zero, desde o back-end até o front-end e o deploy. O objetivo era criar uma solução eficiente para gerenciar o cadastro de pacientes, com autenticação de usuários e operações CRUD (Create, Read, Update, Delete).<br>

🔧 Tecnologias e Ferramentas Utilizadas:
Back-end: Desenvolvi uma API RESTful em Python utilizando o framework Flask, seguindo o paradigma de Programação Orientada a Objetos (POO) para garantir um código modular e de fácil manutenção.<br>
Front-end: Criei uma interface responsiva e intuitiva usando HTML, CSS (com Bootstrap) e JavaScript.
Banco de Dados: Utilizei SQLite para armazenar os dados dos pacientes e dos login, utilizei o SQLAlchemy como ORM, o que permitiu uma interação mais eficiente e segura com o banco de dados, além de facilitar a manutenção do código.<br>
Deploy: Fiz o deploy da aplicação em uma VM (Virtual Machine) na Google Cloud, configurando o Nginx como proxy reverso, Gunicorn como servidor WSGI e Supervisor para gerenciar os processos.<br>
💡 Destaques do Projeto:
Implementei um sistema de autenticação de usuários para garantir acesso seguro ao sistema, com suporte a tokens JWT e uma blacklist para garantir que tokens comprometidos não possam ser reutilizados. Existem dois tipos de usuários no sistema, o usuário que possui acesso total ao sistema e o usuário que apenas cadastra novos pacientes (como visto na última imagem onde tentei excluir um paciente com o usuário com menos permissões e deu não autorizado).<br>
Realizei a integração completa entre o front-end e o back-end, garantindo que todas as operações CRUD funcionassem de forma eficiente.<br>
Este projeto reforçou minhas habilidades em desenvolvimento full-stack, desde a criação de APIs até a entrega de uma aplicação funcional e bem estruturada. Estou muito satisfeito com o resultado e animado para aplicar esses aprendizados em novos desafios! <br>
👨‍💻 Tecnologias: Python, Flask, SQLite, HTML, CSS, Bootstrap, JavaScript, Nginx, Gunicorn, Supervisor, Google Cloud, SQLALchemy, JWT.<br>

**Link do projeto teste: https://goten11fabri-project.onrender.com/**
