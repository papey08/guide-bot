class UserQuery:
        ADD_USER="""
        INSERT INTO tg_user (tg_username)
        VALUES (%s)
        ON CONFLICT (tg_username) DO NOTHING;
        """
        ADD_RESPONSE="""
                INSERT INTO response (user_id, place_id)
                SELECT id, %s FROM tg_user WHERE tg_username = %s;
                """
        FIND_PLACE_BY_CATEGORY_AND_LOCATION = """
        SELECT p.*
        FROM place p
        JOIN place_category pc ON p.id = pc.place_id
        WHERE pc.category = %s AND p.location = %s
        LIMIT 1;
        """
        FIND_PLACE_BY_CATEGORY = """
                SELECT p.*
                FROM place p
                JOIN place_category pc ON p.id = pc.place_id
                WHERE pc.category = %s
                LIMIT 1;
                """