from rest_access_policy import AccessPolicy




"""
Users and related policy
"""

class UsersPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "create", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["put","patch"],
            "principal": "*",
            "effect": "allow",
            'condition': "is_user"
        },
        {
            "action": ["delete"],
            "principal": "group:admin",
            "effect": "allow"
        }
    ]

    def is_user(self, request, view, action) -> bool:
        user = view.get_object()
        return request.id == user.id

class GroupPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","put", "retrieve"],
            "principal": ["group:researcher","group:admin"],
            "effect": "allow"
        },
        {
            "action": ["create", "destroy"],
            "principal": ["group:admin"],
            "effect": "allow"        
        }
    ]

class UsersInformationPolicy(AccessPolicy):
    statements = [
        
        {
            "action": ["list", "put", "retrieve"],
            "principal": "*",
            "effect": "allow",
            "condition": "is_user"
        },
        {
            "action": ["list", "retrieve"],
            "principal": ["group:researcher", "group:publicUser"],
            "effect": "allow"
        },
        {
            "action": ["list","put", "retrieve"],
            "principal": ["group:admin"],
            "effect": "allow"
        }
    ]
    def is_user(self, request, view, action) -> bool:
        user = view.get_object()
        return request.id == user.id

class DisciplinePolicy(AccessPolicy):
    statements = [
        
        {
            "action": ["list", "put", "retrieve"],
            "principal": "*",
            "effect": "allow",
            "condition": "is_user"
        },
        {
            "action": ["list", "retrieve"],
            "principal": ["group:researcher", "group:publicUser"],
            "effect": "allow"
        },
        {
            "action": ["list","put", "retrieve"],
            "principal": ["group:admin"],
            "effect": "allow"
        }
    ]
    def is_user(self, request, view, action) -> bool:
        user = view.get_object()
        return request.id == user.id

class ResearchFieldPolicy(AccessPolicy):
    statements = [
        
        {
            "action": ["list", "put", "retrieve"],
            "principal": "*",
            "effect": "allow",
            "condition": "is_user"
        },
        {
            "action": ["list", "retrieve"],
            "principal": ["group:researcher", "group:publicUser"],
            "effect": "allow"
        },
        {
            "action": ["list","put", "retrieve"],
            "principal": ["group:admin"],
            "effect": "allow"
        }
    ]
    def is_user(self, request, view, action) -> bool:
        user = view.get_object()
        return request.id == user.id

class ResearchEstablishmentPolicy(AccessPolicy):
    statements = [
        
        {
            "action": ["list", "put", "retrieve"],
            "principal": "*",
            "effect": "allow",
            "condition": "is_user"
        },
        {
            "action": ["list", "retrieve"],
            "principal": ["group:researcher", "group:publicUser"],
            "effect": "allow"
        },
        {
            "action": ["list","put", "retrieve"],
            "principal": ["group:admin"],
            "effect": "allow"
        }
    ]
    def is_user(self, request, view, action) -> bool:
        user = view.get_object()
        return request.id == user.id

"""
database and related policy
"""
