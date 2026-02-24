# Social Media API Documentation

## User Model Changes
The `CustomUser` model has been updated to include:
- `following`: A Many-to-Many relationship to `self` (non-symmetrical).

## New Endpoints

### 1. Follow User
- **URL:** `/api/accounts/follow/<int:user_id>/`
- **Method:** `POST`
- **Authentication:** Token Required
- **Description:** Adds the specified user to the current user's following list.

### 2. Unfollow User
- **URL:** `/api/accounts/unfollow/<int:user_id>/`
- **Method:** `POST`
- **Authentication:** Token Required
- **Description:** Removes the specified user from the current user's following list.

### 3. User Feed
- **URL:** `/api/feed/`
- **Method:** `GET`
- **Authentication:** Token Required
- **Description:** Returns a paginated list of posts from all users the current user follows, ordered by the most recent first.
