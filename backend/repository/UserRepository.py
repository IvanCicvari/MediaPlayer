from sqlalchemy.orm import Session
from backend.DALModels import DALUser
from backend.BLModels import BLUser

class UserRepository:
    def get_user_by_id(self, db: Session, user_id: int) -> BLUser:
        # Query the database to get a single user based on user_id
        dal_user = db.query(DALUser).filter(DALUser.user_id == user_id).first()

        # Check if the user exists
        if dal_user:
            # Map the DALUser to a BLUser and return it
            return BLUser(user_id=dal_user.user_id, username=dal_user.username)
        
        # If user not found, return None
        return None

    def get_all_users(self, db: Session):
        # Query the database to get all users
        dal_users = db.query(DALUser).all()

        # Map each DALUser to a BLUser and return a tuple of BLUsers
        return tuple(BLUser(user_id=dal_user.user_id, username=dal_user.username) for dal_user in dal_users)

    def create_user(self, db: Session, first_name: str, last_name: str, username: str, email: str, password: str,
                    profile_image: str = None, bio: str = None, is_verified: bool = False, 
                    subscription_status: str = None):
        # Create a new DALUser instance
        new_user = DALUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            profile_image=profile_image,
            bio=bio,
            is_verified=is_verified,
            subscription_status=subscription_status
            # You can set other attributes here as well
        )

        try:
            # Add the new user to the session and commit the transaction
            db.add(new_user)
            db.commit()
            # Refresh the instance to get the automatically generated values (e.g., user_id, created_at)
            db.refresh(new_user)

            # Map the DALUser to a BLUser and return it
            return BLUser(user_id=new_user.user_id, username=new_user.username)
        except Exception as e:
            # Handle the exception, log it, or raise a custom exception if needed
            print(f"Error in create_user: {e}")

        # If an error occurred, return None or raise an exception based on your application logic
        return None

    def delete_user(self, db: Session, identifier: str, by_username: bool = True):
        # Specify the condition based on whether you are deleting by username or user_id
        condition = (DALUser.username == identifier) if by_username else (DALUser.user_id == identifier)

        # Try to locate the user in the database based on the provided identifier
        user_to_delete = db.uery(DALUser).filter(condition).first()

        if user_to_delete:
            try:
                # Delete the user from the session and commit the transaction
                db.delete(user_to_delete)
                db.commit()
                return True  # Return True to indicate successful deletion
            except Exception as e:
                # Handle the exception, log it, or raise a custom exception if needed
                print(f"Error in delete_user: {e}")

        # If user not found or an error occurred, return False or raise an exception based on your application logic
        return False

