Write a terraform configuration to manage GitHub teams - with the following Role matrix.

   Empty spaces represent the user is not a member of the team

   | Username | Team1 | Team2 | Team3 | Team4 | Team5 | Team6 |
   |----------|-------|-------|-------|-------|-------|-------|
   |User1 | member | maintainer | member | member | maintainer | member |
   |User2 | maintainer | member	| member | maintainer	| member | member |
   |User3 | member | member | maintainer | member | member | member |
   |User4 |  | member | member | member | member | maintainer | 
   |User5 | member |  | member | member |  | member | 
   |User6 | member | member | member | member | member |  |
   |User7 | member | member | member | member | member | member |
   |User8 | member | member |  | member | member | member |
   |User9 | member | member |  | member | member | member |
   |User10 | member | member |  | member | member | member |
   
   Take into consideration ease of maintenance 


# Solution

I use provider [Github](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team) to solve this challenge.

To make sure ease of maintenance:
- Create new team (if not existed)
- Add user to team base on list team_member create list of member of team, If new member involve to new team, add this user to this list 
```
variable "team_member" {
  type = map(list(string))
  default = {
    team1 = [
      "User1",
      "User2",
      "User3",
      "User5",
      ...
    ]
    team2 = [
      "User1",
      "User2",
      "User3",
      ...
    ]
    ...
  }
```
- Assign the maintainer role, by defined who is maintainer in this list
```
locals {
  maintainer_role = {
    team1 = {
      "User2" : "maintainer"
    }
    team2 = {
      "User1" : "maintainer"
    }
    team3 = {
      "User3" : "maintainer"
    }
    team4 = {
      "User2" : "maintainer"
    }
    team5 = {
      "User1" : "maintainer"
    }
    team6 = {
      "User4" : "maintainer"
    }
  }
}
```

My 

# Output

Add user to team

```bash
❯ terraform apply
github_team.teams["team6"]: Refreshing state... [id=11131761]
github_team.teams["team3"]: Refreshing state... [id=11131765]
github_team.teams["team2"]: Refreshing state... [id=11131763]
github_team.teams["team4"]: Refreshing state... [id=11131762]
github_team.teams["team1"]: Refreshing state... [id=11131764]
github_team.teams["team5"]: Refreshing state... [id=11131760]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_team_membership.add_members["11131760-User1"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User1"
    }

  # github_team_membership.add_members["11131760-User10"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User10"
    }

  # github_team_membership.add_members["11131760-User2"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User2"
    }

  # github_team_membership.add_members["11131760-User3"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User3"
    }

  # github_team_membership.add_members["11131760-User4"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User4"
    }

  # github_team_membership.add_members["11131760-User6"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User6"
    }

  # github_team_membership.add_members["11131760-User7"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User7"
    }

  # github_team_membership.add_members["11131760-User8"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User8"
    }

  # github_team_membership.add_members["11131760-User9"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131760"
      + username = "User9"
    }

  # github_team_membership.add_members["11131761-User1"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User1"
    }

  # github_team_membership.add_members["11131761-User10"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User10"
    }

  # github_team_membership.add_members["11131761-User2"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User2"
    }

  # github_team_membership.add_members["11131761-User3"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User3"
    }

  # github_team_membership.add_members["11131761-User4"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User4"
    }

  # github_team_membership.add_members["11131761-User5"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User5"
    }

  # github_team_membership.add_members["11131761-User7"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User7"
    }

  # github_team_membership.add_members["11131761-User8"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User8"
    }

  # github_team_membership.add_members["11131761-User9"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131761"
      + username = "User9"
    }

  # github_team_membership.add_members["11131762-User1"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User1"
    }

  # github_team_membership.add_members["11131762-User10"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User10"
    }

  # github_team_membership.add_members["11131762-User2"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User2"
    }

  # github_team_membership.add_members["11131762-User3"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User3"
    }

  # github_team_membership.add_members["11131762-User4"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User4"
    }

  # github_team_membership.add_members["11131762-User5"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User5"
    }

  # github_team_membership.add_members["11131762-User6"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User6"
    }

  # github_team_membership.add_members["11131762-User7"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User7"
    }

  # github_team_membership.add_members["11131762-User8"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User8"
    }

  # github_team_membership.add_members["11131762-User9"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131762"
      + username = "User9"
    }

  # github_team_membership.add_members["11131763-User1"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User1"
    }

  # github_team_membership.add_members["11131763-User10"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User10"
    }

  # github_team_membership.add_members["11131763-User2"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User2"
    }

  # github_team_membership.add_members["11131763-User3"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User3"
    }

  # github_team_membership.add_members["11131763-User4"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User4"
    }

  # github_team_membership.add_members["11131763-User6"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User6"
    }

  # github_team_membership.add_members["11131763-User7"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User7"
    }

  # github_team_membership.add_members["11131763-User8"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User8"
    }

  # github_team_membership.add_members["11131763-User9"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131763"
      + username = "User9"
    }

  # github_team_membership.add_members["11131764-User1"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User1"
    }

  # github_team_membership.add_members["11131764-User10"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User10"
    }

  # github_team_membership.add_members["11131764-User2"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User2"
    }

  # github_team_membership.add_members["11131764-User3"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User3"
    }

  # github_team_membership.add_members["11131764-User5"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User5"
    }

  # github_team_membership.add_members["11131764-User6"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User6"
    }

  # github_team_membership.add_members["11131764-User7"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User7"
    }

  # github_team_membership.add_members["11131764-User8"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User8"
    }

  # github_team_membership.add_members["11131764-User9"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131764"
      + username = "User9"
    }

  # github_team_membership.add_members["11131765-User1"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131765"
      + username = "User1"
    }

  # github_team_membership.add_members["11131765-User2"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131765"
      + username = "User2"
    }

  # github_team_membership.add_members["11131765-User3"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131765"
      + username = "User3"
    }

  # github_team_membership.add_members["11131765-User4"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131765"
      + username = "User4"
    }

  # github_team_membership.add_members["11131765-User5"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131765"
      + username = "User5"
    }

  # github_team_membership.add_members["11131765-User6"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131765"
      + username = "User6"
    }

  # github_team_membership.add_members["11131765-User7"] will be created
  + resource "github_team_membership" "add_members" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = "11131765"
      + username = "User7"
    }

Plan: 53 to add, 0 to change, 0 to destroy.
```
Assign role mantainer for specifics user
```bash
>  terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
with the following symbols:
  + create

Terraform will perform the following actions:

  # github_team_membership.add_maintainer["team1"] will be created
  + resource "github_team_membership" "add_maintainer" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = "11131859"
      + username = "User2"
    }

  # github_team_membership.add_maintainer["team2"] will be created
  + resource "github_team_membership" "add_maintainer" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = "11131863"
      + username = "User1"
    }

  # github_team_membership.add_maintainer["team3"] will be created
  + resource "github_team_membership" "add_maintainer" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = "11131861"
      + username = "User3"
    }

  # github_team_membership.add_maintainer["team4"] will be created
  + resource "github_team_membership" "add_maintainer" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = "11131862"
      + username = "User2"
    }

  # github_team_membership.add_maintainer["team5"] will be created
  + resource "github_team_membership" "add_maintainer" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = "11131857"
      + username = "User1"
    }

  # github_team_membership.add_maintainer["team6"] will be created
  + resource "github_team_membership" "add_maintainer" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = "11131858"
      + username = "User4"
    }
 ...
```

# How to run
```bash
terraform init
terraform plan -var 'github_token=<GITHUB_TOKEN>'
```