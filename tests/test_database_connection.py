from pytest import mark

@mark.it("Database is initilaised with seed")
def test_database_connection_initialisation(db_conn):
    test_seed_path = "seeds/test_seed.sql"
    db_conn.seed(test_seed_path)

    actual_result = db_conn.execute("select * from test_shows")

    expected_result = [
            {'id': 1, 'name':'Invincible', 'rating':9},
            {'id': 2, 'name':'Demolition', 'rating':10},
            {'id': 3, 'name':'Better Call Saul', 'rating':10},
    ]

    assert actual_result == expected_result
        


    
