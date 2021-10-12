class ErrorConfig:
    get_more_params = "http://127.0.0.1:8000/{operation}/?{params}=?,?,?,?,? Please will be use correct {params} parameter(max=1)"
    not_correct_params = "http://127.0.0.1:8000/{operation}/?{params}=?,?,?,?,? Please will be use correct {params} parameter"

    post_more_params = "http://127.0.0.1:8000/{operation}/?{params}=?,?,?,?,? Please will be use correct {params} parameter(max=5,min=2)"

    empty_username = "Please will be not use empty username parameter"
    empty_password = "Please will be not use empty password parameter"
    empty_username_password = "Please do not leave the username and password fields empty"
