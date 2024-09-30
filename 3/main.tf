# GitHub Provider Configuration
provider "github" {
  token        = var.github_token
  organization = var.github_org
}

# Centralized definition for all teams
locals {
  teams = {
    team1 = "Team 1"
    team2 = "Team 2"
    team3 = "Team 3"
    team4 = "Team 4"
    team5 = "Team 5"
    team6 = "Team 6"
  }
}

# Defined role
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

# Map user to team
locals {
  map_user_team = flatten([
    for team_name, members in var.team_member : [
      for member in members : {
        team_id  = github_team.teams[team_name].id
        username = member
      }
    ]
  ])
}


# Create GitHub teams 
resource "github_team" "teams" {
  for_each    = local.teams
  name        = each.value
  description = "GitHub team ${each.value}"
}

# Add members to team
resource "github_team_membership" "add_members" {
  for_each = { for membership in local.map_user_team : "${membership.team_id}-${membership.username}" => membership }
  
  team_id  = each.value.team_id
  username = each.value.username
  role     = "member"
}

# Add maintaner
resource "github_team_membership" "add_maintainer" {
  for_each = local.maintainer_role

  team_id  = github_team.teams[each.key].id  # Map the team ID
  username = keys(each.value)[0]             # Fetch the username from the map
  role     = each.value[keys(each.value)[0]] # Fetch the corresponding role (e.g., maintainer)
}
