# Django-Movie-Recommendatio

This recommender app is a python application that generates movie recommendations.

This movie recommendations are provided in a CSV. The site does not host actual movies but its is a recommendation engine using regular code and a database. 

This recommendation engine does not use Machine Learning.......yet 😂😂
To make the recommendation actually work, I needed to first mark the movies a user has watched using Django Admin site. Then I wrote a recommendation algorithm based on your watched movies.

## Marking Watched Movies In Django Admin
* Run Django Server
* visit admin url app_url/admin
* ![image](https://user-images.githubusercontent.com/69109175/160308836-62edfa21-c8cb-44fc-8cf7-fcd95f19a536.png)
* Then you click into the movie entry and mark it as watched and press Save.

## Run make_recommendations CMD to Generate Recommendations
For any recommendation systems, the key idea is always to come up with a good algorithm/model to predict if a specific user will like or dislike his/her unseen item, as shown in the following screenshot:

![image](https://user-images.githubusercontent.com/69109175/160308950-82f01992-23fc-4bce-8adf-fa710d736c9d.png)

There are probably hundreds of good recommendation algorithms and can be roughly divided into two categories:

### Content filtering based: 
The content filtering based recommendation algorithms assume you may like a new movie if you have watched very similar movies before. Or based on your user profile (like age, gender, interests), it will try to find new movies matching your profile.

### Collaborative filtering based: 
The collaborative filtering algorithms assume you may like a new movie if other users similar to you (similar profile or watched similar movies) have watched this movie.
In this project, we will use content filtering based algorithm, and we will try to recommend unwatched/new movies to you if they are similar to your watched movies.

## How do we calculate such movie similarity
Here we will use Jaccard similarity which is probably the simplest but very effective method to calculate similarity between two sets.

Jaccard Similarity is defined as the size of intersection of two sets divided by the size of union of that two sets.
