#!/usr/bin/env python3

icecream= [{"_id":"5f6a07f03cf7c683e5fd6ff3","index":0,"guid":"866cb8b7-dd6a-48b2-8e57-06eac94047d7","isActive":True,"balance":"$1,718.12","picture":"http://placehold.it/32x32","age":25,"eyeColor":"green","name":"Klein Whitaker","gender":"male","company":"TEMORAK","email":"kleinwhitaker@temorak.com","phone":"+1 (979) 514-2430","address":"477 Llama Court, Centerville, Georgia, 760","about":"Exercitation sit mollit nulla labore occaecat est. Sint cillum ad aliqua eiusmod et id magna. Culpa eu amet quis dolor dolor incididunt enim. Eu occaecat velit esse amet non nostrud voluptate et duis aute pariatur.\r\n","registered":"2016-11-14T01:15:43 +05:00","latitude":65.894247,"longitude":-137.805434,"tags":["deserunt","aute","in","laborum","nulla","ad","minim"],"friends":[{"id":0,"name":"Suzette Coffey"},{"id":1,"name":"Munoz Alston"},{"id":2,"name":"Gilmore Mathis"}],"greeting":"Hello, Klein Whitaker! You have 6 unread messages.","favoriteFruit":"banana"},{"_id":"5f6a07f07d1e1f367a062d89","index":1,"guid":"80c09c64-0482-4908-a2f4-56d1845c8a76","isActive":False,"balance":"$3,699.87","picture":"http://placehold.it/32x32","age":40,"eyeColor":"green","name":"Marietta Gates","gender":"female","company":"ACCUFARM","email":"mariettagates@accufarm.com","phone":"+1 (951) 472-2292","address":"615 Oxford Walk, Wheaton, New Jersey, 9351","about":"Eu occaecat ut sunt duis velit exercitation nulla id nisi sint sunt. Culpa irure irure est officia ut duis tempor. Incididunt duis adipisicing culpa laboris incididunt laboris occaecat amet fugiat elit aliqua labore. Consequat nisi Lorem esse reprehenderit cillum.\r\n","registered":"2016-11-29T10:26:06 +05:00","latitude":-67.521965,"longitude":171.850314,"tags":["duis","laborum","non","nisi","ad","commodo","est"],"friends":[{"id":0,"name":"Christina Roman"},{"id":1,"name":"Louella Jacobs"},{"id":2,"name":"Terrie Miles"}],"greeting":"Hello, Marietta Gates! You have 3 unread messages.","favoriteFruit":"strawberry"},{"_id":"5f6a07f0f199653dd3632555","index":2,"guid":"59fca3e1-ddec-47cb-9c8c-6677fc871592","isActive":True,"balance":"$3,919.41","picture":"http://placehold.it/32x32","age":21,"eyeColor":"brown","name":"Mariana Mays","gender":"female","company":"ACIUM","email":"marianamays@acium.com","phone":"+1 (993) 496-3505","address":"844 Pooles Lane, Cedarville, Wyoming, 1922","about":"Veniam irure pariatur cillum eu non culpa exercitation eiusmod et. In fugiat consequat laborum fugiat laboris deserunt. Eiusmod consequat nulla culpa reprehenderit ut incididunt do reprehenderit.\r\n","registered":"2017-08-21T11:42:15 +04:00","latitude":-40.939371,"longitude":-24.70741,"tags":["proident","dolor","nulla","eiusmod","do","enim","dolor"],"friends":[{"id":0,"name":"Verna Stanton"},{"id":1,"name":"Craig Olsen"},{"id":2,"name":"Banks William"}],"flavor":"salty","favoriteFruit":"banana"},{"_id":"5f6a07f0673341d93bf65a05","index":3,"guid":"3e882428-fd37-4362-a938-f5abf918c28a","isActive":False,"balance":"$2,308.90","picture":"http://placehold.it/32x32","age":29,"eyeColor":"brown","name":"Antoinette Carr","gender":"female","company":"ETERNIS","email":"antoinettecarr@eternis.com","phone":"+1 (804) 543-2347","address":"159 Quincy Street, Ezel, Alaska, 3056","about":"Officia non ea duis reprehenderit do eu pariatur eu duis exercitation proident eu aute. Sit reprehenderit mollit cupidatat eu tempor ut minim laborum non commodo. Amet consequat aute duis officia ipsum.\r\n","registered":"2017-05-23T04:56:59 +04:00","latitude":43.77431,"longitude":151.483133,"tags":["minim","aliquip","in","consequat","anim","ipsum","id"],"friends":[{"id":0,"name":"Spencer Sykes"},{"id":1,"name":"Josefina Best"},{"id":2,"name":"Carlson Hernandez"}],"greeting":"Hello, Antoinette Carr! You have 3 unread messages.","favoriteFruit":"strawberry"},{"_id":"5f6a07f0518bc7e0b0f0bd2a","index":4,"guid":"26a8b683-0c5b-4b4e-9ed3-3e067677cd59","isActive":True,"balance":"$2,884.67","picture":"http://placehold.it/32x32","age":34,"eyeColor":"brown","name":"Chase Hodge","gender":"male","company":"FURNIGEER","email":"chasehodge@furnigeer.com","phone":"+1 (975) 406-3779","address":"351 Franklin Street, Hailesboro, Guam, 8625","about":"Do dolore do duis aliqua mollit veniam commodo est amet voluptate et mollit exercitation do. Est exercitation dolore qui ut tempor aliquip non deserunt nisi Lorem est laboris. Incididunt voluptate elit veniam cupidatat qui. Fugiat quis voluptate dolor dolore minim quis.\r\n","registered":"2015-11-02T02:06:41 +05:00","latitude":-47.397924,"longitude":-66.351064,"tags":["ipsum","ipsum","aliqua","labore","proident","cupidatat","nisi"],"friends":[{"id":0,"name":"Jami Ramsey"},{"id":1,"name":"Mckenzie Snow"},{"id":2,"name":"Hampton Solomon"}],"greeting":"Hello, Chase Hodge! You have 6 unread messages.","favoriteFruit":"apple"}]
icecream.append(99)
user_name= input("What is your name, good sir/madam/etc.?")
print(f"{icecream[-1]} flavors, and {user_name} chooses to be {icecream[2]['flavor']}.")

