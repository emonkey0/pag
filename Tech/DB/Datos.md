# Usuario
***Usuarios Necesarios únicamente para registro***

| id             | User    | Contra         | nickName      |
| -------------- | ------- | -------------- | ------------- |
| idUsuarioUnico | Usuario | Contra Cifrada | apodo usuario |
***Opcionales a menos que se activen funciones extras***

| email                            | telefono            |
| -------------------------------- | ------------------- |
| correo para logeo y verificacion | telefono para logeo |

***Logeos del usuario atreves del tiempo en la cuenta***

| `first_name: str`      | last_name: str           | last_login: Optional[datetime]                           | is_active: bool                                            | is_verified: bool                                                                                                      | role: str                                                                                              | password_reset_token: str                                      | password_reset_expires: Optional[datetime]                                  |
| ---------------------- | ------------------------ | -------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | --------------------------------------------------------------------------- |
| El nombre del usuario. | El apellido del usuario. | La fecha y hora del último inicio de sesión del usuario. | Un indicador de si la cuenta del usuario está activa o no. | Un indicador de si el usuario ha verificado su cuenta, por ejemplo, a través de un correo electrónico de confirmación. | El rol o nivel de acceso del usuario (por ejemplo, "editor",""usuario", "moderador", "administrador"). | Un token utilizado para restablecer la contraseña del usuario. | La fecha y hora de vencimiento del token de restablecimiento de contraseña. |


### Tabla Fotos

| idFoto | Foto       | idUsuario            | Descripcion                           |
| ------ | ---------- | -------------------- | ------------------------------------- |
| id     | /url o BOB | idUsuario Dueño Foto | Descripcion para busqueda del usuario |
