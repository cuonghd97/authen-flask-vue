SERVER_ERROR_500 = ({'message': 'Internal server error'}, 500)
NOT_FOUND_404 = ({'message': 'Resource could not be found'}, 404)
NO_INPUT_400 = ({'message': 'No input data provided'}, 400)
INVALID_INPUT_422 = ({'message': 'Invalid input'}, 422)
ALREADY_EXISTS = ({'message': 'Already exists'}, 409)
DOES_NOT_EXIST = ({'message': 'Does not exist'}, 409)
NOT_ADMIN = ({'message': 'Admin permission denied'}, 999)
HEADER_NOT_FOUND = ({'message': 'Header does not exists'}, 999)
WRONG_PASSWORD = ({'message': "Wrong password"}, 999)
