#!/bin/python3

# i just saved myself 100$ a month!! 

import requests
import random

s = requests.Session();

def genCsrfToken():
    ctkn = ""
    for i in range(0, 32):
        ctkn += random.choice("abcdef1234567890")
    return ctkn
    
    
REQUEST_HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
          "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"}

    
def login(username, password, phoneNo):
    global REQUEST_HEADERS
    s.get("https://twitter.com/")
    
    r = s.post("https://api.twitter.com/1.1/guest/activate.json", headers=REQUEST_HEADERS, json={})
    
    guestToken = r.json()['guest_token']
    s.cookies.set("gt", guestToken, domain=".twitter.com")
    REQUEST_HEADERS["x-guest-token"] = guestToken
    
    r = s.post("https://api.twitter.com/1.1/onboarding/task.json?flow_name=login", headers=REQUEST_HEADERS, json={
          "input_flow_data": {
            "flow_context": {
              "debug_overrides": {},
              "start_location": {
                "location": "unknown"
              }
            }
          },
          "subtask_versions": {
            "action_list": 2,
            "alert_dialog": 1,
            "app_download_cta": 1,
            "check_logged_in_account": 1,
            "choice_selection": 3,
            "contacts_live_sync_permission_prompt": 0,
            "cta": 7,
            "email_verification": 2,
            "end_flow": 1,
            "enter_date": 1,
            "enter_email": 2,
            "enter_password": 5,
            "enter_phone": 2,
            "enter_recaptcha": 1,
            "enter_text": 5,
            "enter_username": 2,
            "generic_urt": 3,
            "in_app_notification": 1,
            "interest_picker": 3,
            "js_instrumentation": 1,
            "menu_dialog": 1,
            "notifications_permission_prompt": 2,
            "open_account": 2,
            "open_home_timeline": 1,
            "open_link": 1,
            "phone_verification": 4,
            "privacy_options": 1,
            "security_key": 3,
            "select_avatar": 4,
            "select_banner": 2,
            "settings_list": 7,
            "show_code": 1,
            "sign_up": 2,
            "sign_up_review": 4,
            "tweet_selection_urt": 1,
            "update_users": 1,
            "upload_media": 1,
            "user_recommendations_list": 4,
            "user_recommendations_urt": 1,
            "wait_spinner": 3,
            "web_modal": 1
          }
        })
        
    flowToken = r.json()["flow_token"]
    
    s.post("https://api.twitter.com/1.1/branch/init.json", headers=REQUEST_HEADERS, json={})
    
    s.get("https://twitter.com/i/js_inst?c_name=ui_metrics")
    
    # step 1
    
    r = s.post("https://api.twitter.com/1.1/onboarding/task.json", headers=REQUEST_HEADERS, json={
      "flow_token": flowToken,
      "subtask_inputs": [
        {
          "subtask_id": "LoginJsInstrumentationSubtask",
          "js_instrumentation": {
            "response": "{\"rf\":{\"a0060f183481e46d5129ec3ade82eb75c7ce63d039855f3edec7ece303b10fee\":115,\"a6d6530258ba692474bdf1f8bf32c70349459a907174658fe020f8ff3f7dcee6\":-5,\"af27e4608e1681e7e2e28f6405f11316632765622cbb1fa4a045c65ea50d56b3\":-1,\"a3bd810c6adff505ead0e380870f006a6a24f33f4725995209290eb9b6b50fc8\":0},\"s\":\"lALI5arFoKGSZlZ1WzzZ6kkUEJ3-WMWhgyERGN4ZjNLlI49vW63O721HJKx69997FTxCzMwoHSyV8xIJVEax1P0bCFwEZQJQLme1dtHhkB7jjp_JC0NCXwHdkoV2dT1s_EEZRb7eAvAOUgKMZq7VZFDL5zWYUoxvQBL4bpclWKadurJyWfizc5et8oHeMk_yunhHvvmxk6MCFQ7qJchwA1T_qhnV2vHMTCGpzMGybjn4hb2okHP64CC-AkbpQJWBBTBGNGCJst1I3Li7tLUui_WhRenRxsuQlSlhIGLyR1OerFpqKzyep1LH0L2BAGdAIbcGtOdUSIB-WUEQgKieLwAAAYYa6yHj\"}",
            "link": "next_link"
          }
        }
      ]
    })
    flowToken = r.json()["flow_token"]
    
    # step 2
    
    r = s.post("https://api.twitter.com/1.1/onboarding/task.json", headers=REQUEST_HEADERS, json={
      "flow_token": flowToken,
      "subtask_inputs": [
        {
          "subtask_id": "LoginEnterUserIdentifierSSO",
          "settings_list": {
            "setting_responses": [
              {
                "key": "user_identifier",
                "response_data": {
                  "text_data": {
                    "result": username
                  }
                }
              }
            ],
            "link": "next_link"
          }
        }
      ]
    })
    flowToken = r.json()["flow_token"]
    
    # step 3
    
    r = s.post("https://api.twitter.com/1.1/onboarding/task.json", headers=REQUEST_HEADERS, json={
      "flow_token": flowToken,
      "subtask_inputs": [
        {
          "subtask_id": "LoginEnterPassword",
          "enter_password": {
            "password": password,
            "link": "next_link"
          }
        }
      ]
    })
    flowToken = r.json()["flow_token"]
    
    # step 4
    r = s.post("https://api.twitter.com/1.1/onboarding/task.json", headers=REQUEST_HEADERS, json={
      "flow_token": flowToken,
      "subtask_inputs": [
        {
          "subtask_id": "AccountDuplicationCheck",
          "check_logged_in_account": {
            "link": "AccountDuplicationCheck_false"
          }
        }
      ]
    })
    flowToken = r.json()["flow_token"]
    
    # check if im being asked for my phone number
    if r.content.find(b"telephone") != -1:
        r = s.post("https://api.twitter.com/1.1/onboarding/task.json", headers=REQUEST_HEADERS, json={
          "flow_token": flowToken,
          "subtask_inputs": [
            {
              "subtask_id": "LoginAcid",
              "enter_text": {
                "text": phoneNo,
                "link": "next_link"
              }
            }
          ]
        }
    
    csrfToken = genCsrfToken()
    del REQUEST_HEADERS['x-guest-token']
    
    REQUEST_HEADERS["x-csrf-token"] = csrfToken
    REQUEST_HEADERS["x-twitter-active-user"] = "yes"
    REQUEST_HEADERS["x-twitter-auth-type"] = "OAuth2Session"
    REQUEST_HEADERS["x-twitter-client-language"] = "en"
    
    s.cookies.set("ct0", csrfToken, domain=".twitter.com")    
    r = s.post("https://api.twitter.com/1.1/jot/client_event.json?keepalive=false", headers=REQUEST_HEADERS, data="debug=true&log=%5B%7B%22_category_%22%3A%22client_event%22%2C%22format_version%22%3A2%2C%22triggered_on%22%3A1675493918049%2C%22items%22%3A%5B%5D%2C%22event_namespace%22%3A%7B%22page%22%3A%22compose%22%2C%22section%22%3A%22composition%22%2C%22element%22%3A%22send_tweet%22%2C%22action%22%3A%22click%22%2C%22client%22%3A%22m5%22%7D%2C%22client_event_sequence_start_timestamp%22%3A1675493550691%2C%22client_event_sequence_number%22%3A102%2C%22client_app_id%22%3A%223033300%22%7D%5D")

    csrfToken = s.cookies.get_dict()["ct0"]
    REQUEST_HEADERS["x-csrf-token"] = csrfToken
    
def tweet(msg):
    global REQUEST_HEADERS
    gqlEndpoint = "MYy_64Dv_JRBlPN5OZjQXw" 
    
    
    r = s.post("https://api.twitter.com/graphql/"+gqlEndpoint+"/CreateTweet", headers=REQUEST_HEADERS, json={
      "variables": {
        "tweet_text": msg,
        "dark_request": False,
        "media": {
          "media_entities": [],
          "possibly_sensitive": False
        },
        "withDownvotePerspective": False,
        "withReactionsMetadata": False,
        "withReactionsPerspective": False,
        "withSuperFollowsTweetFields": True,
        "withSuperFollowsUserFields": True,
        "semantic_annotation_ids": []
      },
      "features": {
        "longform_notetweets_consumption_enabled": True,
        "tweetypie_unmention_optimization_enabled": True,
        "vibe_api_enabled": True,
        "responsive_web_edit_tweet_api_enabled": True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
        "view_counts_everywhere_api_enabled": True,
        "interactive_text_enabled": True,
        "responsive_web_text_conversations_enabled": False,
        "responsive_web_twitter_blue_verified_badge_is_enabled": True,
        "verified_phone_label_enabled": False,
        "freedom_of_speech_not_reach_appeal_label_enabled": False,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_enhance_cards_enabled": False
      },
      "queryId": gqlEndpoint
    })
    