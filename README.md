# KMDB

Aplicação para gerenciar usuários, filmes e reviews.


### Endpoints da aplicação:
| Método | Endpoint | Objetivo | Autorização Token |
|---|---|---|---|
| `POST` | `/api/users/register/` |Criação de um crítico de filmes ou de um usuário comum | `Não` |
| `POST` | `/api/login/` |Autenticar um usuário e retornar um token de acesso | `Não` |
| `GET` | `/api/users/` |Listar todos os usuários | `Sim` |
| `GET` | `/api/users/<int:user_id>/` | Filtrar um usuário | `Sim` |
| `GET` | `/api/movies/` |Listar todos os filmes | `Não` |
| `POST` | `/api/movies/` |Criação de um filme | `Sim` |
| `GET` | `/api/movies/<int:movie_id>/` |Filtrar um filme | `Não` |
| `DELETE` | `/api/movies/<int:movie_id>/` |Deletar um filme | `Sim` |
| `PATCH` | `/api/movies/<int:movie_id>/` |Atualizar um filme | `Sim` |
| `POST` | `/api/movies/<int:movie_id>/reviews/` |Criação de uma nova review para o filme | `Sim` |
| `GET` | `/api/movies/<int:movie_id>/reviews/` |Listagem das reviews do filme em questão | `Não` |
| `GET` | `/api/movies/<int:movie_id>/reviews/<int:review_id>/` |Filtragem da review do filme em questão | `Não` |
| `DELETE` | `/api/movies/<int:movie_id>/reviews/<int:review_id>/` |Deleção da review do filme em questão | `Sim` |

### Diagrama de Entidade de Relacionamento

<img src="https://i.imgur.com/xOEdmGH.png" width="70%" height="500px">
