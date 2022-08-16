from app import app           ## to look into later 



def test1():                                    ## juste see if we are getting the right respond for opening our page  
    response = app.test_client().get("/")
    assert response.status_code == 200 


def test2():                                      
    response = app.test_client().get("/base")   ## it's the same juste applied on the /base page 
    assert response.status_code == 200 
