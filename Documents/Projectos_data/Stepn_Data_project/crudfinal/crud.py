import click
import json
import json_manager

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='Nombre de usuario')
@click.option('--last', required=True, help='Apellido de usuario')
@click.pass_context
def nuevo(ctx, name, last):
    if not name or not last:
        ctx.fail('Rellenar campos de usuario')
    else:
        data = read_json()
        new_id = len(data) + 1  # autoincrementar el ID por nuevo registro
        nuevo_usuario = {
            'id': new_id,
            'name': name,
            'last': last
        }
        data.append(nuevo_usuario)
        write_json(data)
        print(f"El usuario {name} {last} se creó correctamente con el ID {new_id}")


@cli.command()
def users():
    users = read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['last']}")


@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"El ID {id}, no existe para ningún usuario")
    else:
        print(f"El ID {id} pertenece al usuario {user['name']} {user['last']}")


@cli.command()
@click.option('--name', help='Nombre de usuario')
@click.option('--last', help='Apellido de usuario')
@click.pass_context
@click.argument('id', type=int)
def update(ctx, id, name, last):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if last is not None:
                user['last'] = last
            break
    json_manager.write_json(data)
    print(f"Se ha actualizado con éxito al usuario con ID {id}. Ahora el ID {id} pertenece a {user['name']} {user['last']}")


@cli.command()
@click.argument('id', type=int)
def borrar(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"El ID {id}, no existe para ningún usuario")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"El usuario {user['name']} {user['last']} cuyo ID era {id} se ha borrado de la base de datos con éxito")


def read_json():
    with open('data.json') as f:
        data = json.load(f)
    return data

def write_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    cli()
