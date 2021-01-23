from flask import Flask, jsonify, request, abort
import sys

from models import db, setup_db, Clothes



app = Flask(__name__)
setup_db(app)




@app.route('/')
def index():
    return jsonify({'response': 'Sarah preloved website'})

@app.route('/clothes', methods=['GET'])
def clothes():
    response = {}
    clothes = Clothes.query.all()
    response['clothes'] = [a.format() for a in clothes]
    response['success'] = True
    return jsonify(response)

@app.route('/clothes/<int:id>', methods=['GET'])
def item(id):
    response = {}
    item = Clothes.query.get(id)
    if item:
        response['item'] = item.format()
        response['success'] = True
    else:
        abort(404)
    return jsonify(response)

@app.route('/clothes/<int:id>', methods=['PATCH'])
def item_update(id):
    response = {}
    response['item keys'] = ""
    item = Clothes.query.get(id)
    if item:
        body = request.get_json()
        if body:
            for a in body.keys():
                if a in item.format().keys():
                    pass
                else:
                    response['message'] = 'wrong insert'
                if body.get('name'):
                    item.name=body.get('name')
                if body.get('price'):
                    item.price=body.get('price')
                if body.get('pieces'):
                    item.pieces=body.get('pieces')
                if body.get('immage_link'):
                    item.immage_link=body.get('immage_link')
                try:
                    item.update()
                    response['id'] = item.id
                except:
                    print(sys.exc_info())
                    abort(500)
                finally:
                    item.sesion_close()
            response['success'] = True
        else:
            print(sys.exc_info())
            abort(400)
    else:
        abort(404)
    return jsonify(response)

@app.route('/clothes', methods=['POST'])
def post_clothes():
    response = {}
    body = request.get_json()
    if body:
        name = body.get('name')
        price = body.get('price')
        pieces = body.get('pieces')
        immage_link = body.get('immage_link')
    else:
        abort(200)
    try:
        cloth = Clothes(name=name, price=price, pieces=pieces, immage_link=immage_link)
        cloth.insert()
        response['success'] = True
        response['id'] = cloth.id
    except:
        abort(500)
        print(sys_exc_log())
    finally:
        cloth.sesion_close()
    return jsonify(response)

@app.route('/clothes/<int:id>', methods=['DELETE'])
def delete_clothes(id):
    response = {}
    item = Clothes.query.get(id)
    if item:
        try:
            item.delete()
            response['success'] = True
            response['id'] = item.id
        except:
            print(sys.exc_info())
            abort(500)
        finally:
            item.sesion_close()
    else:
        abort(407)
    return jsonify(response)





@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad Request'
    }), 400

@app.errorhandler(401)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'Unauthorized'
    }), 401

@app.errorhandler(403)
def forbiden(error):
    return jsonify({
        'success': False,
        'error': 403,
        'message': 'Forbiden'
    }), 403


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Not Found'
    }), 404


@app.errorhandler(405)
def method_now_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'Method Not Allowed'
    }), 405


@app.errorhandler(422)
def unprocesable_entity(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'Unprocesable Entity'
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Server Error'
    }), 500
