# Verificação da adaptação conservadora

58 verificações de integração passaram com Python 3.12.14.

O código do bloco __main__ de app.py foi executado sem alterações, numa pasta de instância e base SQLite temporárias. Flask.run foi substituído apenas no processo de verificação para evitar abrir uma porta. Um segundo processo confirmou persistência e ausência de duplicação do admin.

- actual_main_initialization_and_related_tables
- jwt_required_get_/tarefas
- jwt_required_post_/tarefas
- jwt_required_get_/tarefas/1
- jwt_required_put_/tarefas/1
- jwt_required_delete_/tarefas/1
- register_a
- register_b
- duplicate_email
- reject_admin_registration
- missing_registration_field
- null_password
- empty_username
- wrong_credentials
- missing_login_password
- login_a
- login_b
- login_admin
- token_identifies_id_and_type
- create_a
- create_b
- create_admin
- automatic_ownership_for_both_roles
- reject_owner_field
- invalid_state
- empty_title
- null_title
- missing_description
- list_only_a
- list_only_b
- admin_lists_all
- orm_relationship_both_directions
- owner_reads
- other_user_cannot_read
- other_user_cannot_update
- other_user_cannot_delete
- owner_updates
- admin_reads_other
- admin_updates_other
- put_requires_all_fields
- cannot_change_owner
- invalid_put_state
- invalid_request_preserves_record
- missing_task_get
- missing_task_put
- missing_task_delete
- admin_deletes_other
- deleted_is_missing
- owner_deletes_own
- invalid_jwt
- expired_token
- no_existing_account
- database_role_controls_access
- unicode_register
- unicode_login
- logout
- revoked_token
- new_process_persistence_and_single_admin

Foram ainda conferidos a sintaxe de todos os módulos, a cobertura dos guias, os links locais e os corpos JSON dos pedidos Bruno. O Bruno de desktop não foi executado. As versões das bibliotecas são as presentes no ambiente do export: Flask 3.1.3, Flask-RESTful 0.3.10, Flask-SQLAlchemy 3.1.1 e Flask-JWT-Extended 4.7.4.
