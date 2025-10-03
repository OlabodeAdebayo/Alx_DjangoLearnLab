Blog Post Management
--------------------

Endpoints:
- GET  /posts/               -> list all posts
- GET  /posts/<pk>/          -> view a single post
- GET  /posts/new/           -> create form (login required)
- POST /posts/new/           -> create post (login required)
- GET  /posts/<pk>/edit/     -> edit form (author only)
- POST /posts/<pk>/edit/    -> update post (author only)
- GET  /posts/<pk>/delete/   -> delete confirmation (author only)
- POST /posts/<pk>/delete/   -> deletes post (author only)

Permissions:
- Create: authenticated users only
- Edit/Delete: only the post author
- Read: public

How author is assigned:
- On form submission (CreateView) the view sets `form.instance.author = request.user`.

