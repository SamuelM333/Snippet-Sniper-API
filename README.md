# Snippet sniper API 

## To do

- [x] ~~Add a licence~~
- [ ] Implement OAuth2
- [ ] Encryption
- [ ] Create GitBook
- [ ] Expose API only to HTTPS (SSL)
- [ ] Make models
- [ ] Try mLab
    
## Sinppet structure

- Title
- Body
    - Code
    - Markdown
- Comments

## Models structure

- User
    - name
    - lastname
    - email
    - password
    - date joined
    - last online
    - tokens
- Snippet
    - user
    - title
    - code
    - description
    - comments
        - user
        - text
    - scope
