# Snippet sniper API 

## To do

- [x] ~~Add a licence~~
- [ ] Implement OAuth2
- [x] ~~Encryption~~
- [ ] Secure endpoints
- [ ] Validate fields
- [ ] Add slugs to snippets
- [ ] Create GitBook
- [ ] Expose API only to HTTPS (SSL)
- [x] Make models
- [ ] Get available code languages
- [ ] Check out [Eve Genie] (https://github.com/drud/evegenie)
    
## Snippet structure

- Title
- Body
    - Fragments
        - Language
        - Code

## Models structure

- User
    - name
    - last name
    - email
    - password
    - date joined
    - last online
    - tokens
- Snippet
    - owner
    - title
    - body
    - created
