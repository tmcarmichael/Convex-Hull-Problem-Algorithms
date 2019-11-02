#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <map>
#include <ctime>
using namespace std;


/************************************************
 * Functions for reading the input
 * Students are not recommended to change this part
 ************************************************/
void ReadInput (int &n, int &d, vector< vector<float> >  &point) {
    
    point.clear(); // make the vector point empty;
    float tempfloat;
    
    // Open file and read input from the file
    cin >> n >> d; // input the number of points and dimension
    
    for(int i=0; i<n; i++) {
        vector<float> temppoint;
        for (int j=0; j<d; j++) {
            cin >> tempfloat;
            temppoint.push_back(tempfloat);
        }
        point.push_back(temppoint);
    }
}



void ReadInput (string input_file_name, int &n, int &d, vector< vector<float> >  &point) {
    
    point.clear(); // make the vector point empty;
    float tempfloat;
    
    // Open file and read input from the file
    ifstream myfile (input_file_name.c_str());
    
    if (myfile.is_open())
    {
        myfile >> n >> d; // input the number of points and dimension
        
        for(int i=0; i<n; i++) {
            vector<float> temppoint;
            for (int j=0; j<d; j++) {
                myfile >> tempfloat;
                temppoint.push_back(tempfloat);
            }
            point.push_back(temppoint);
        }
        
        myfile.close();
    }
    else cerr << "Unable to open file";

}


/************************************************
 * Below are some examples of the algorithms.
 * Students are recommended to try to understand them.
 ************************************************/

/*
 *  First example. Very slow.
 */

int SimpleAlgo1 (int &n, int &d, vector< vector<float> >  &point)
{
    vector<bool> isBest(n+1, true);
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            
            // We will check if point[i] is strictly worse than point[j]
            // no need to check if we already know that point[i] is not the best
            //if (isBest[i]) { // Should do this, but let's say we don't
            bool worse_somewhere=false; // This variable will be true if p_i is worse than p_j in some coordinate; i.e., there is k such that p_i[k]<p_j[k]
            
            for (int k=0; k<d; k++)
                if (point[i][k]<point[j][k])
                    worse_somewhere=true;
            // if point[i] is worse than point[j] at coordinate k then we set worse_somewhere to be true
            
            bool not_better=true; // This variable will be true if p_i is note better than p_j in all coordinate; i.e., for all k, p_i[k]<=p_j[k]
            for (int k=0; k<d; k++)
                if (point[i][k]>point[j][k])
                    not_better=false;
            // if point[i] is better than point[j], then not_better=true;
            
            // if point[i] is not better than point[j] and point[i] is actually worse in some dimension, then point[i] is not the best
            if (worse_somewhere && not_better) {
                isBest[i]=false;
            }
            //}
        }
    }
    
    // Count the number of interesting points
    
    int count=0;
    for (int i=0; i<n; i++)
        if (isBest[i]) 
            count++;

    
    // This part is used to check the output. It is not necessary
    for (int i=0; i<n; i++)
        if (isBest[i]) {
            for (int k=0; k<d; k++)
                cout << point[i][k] << " ";
            cout << endl;
        }
    
    return count;
     
}


/*
 *  Second example. Still pretty slow.
 */

int SimpleAlgo2 (int &n, int &d, vector< vector<float> >  &point)
{
    vector<bool> isBest(n+10, true);
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            
            // We will check if point[i] is strictly worse than point[j]
            // no need to check if we already know that point[i] is not the best
            if (isBest[i]) { // *** This is the only additional line from the previous algorithm
                bool worse_somewhere=false; // This variable will be true if p_i is worse than p_j in some coordinate; i.e., there is k such that p_i[k]<p_j[k]
                
                for (int k=0; k<d; k++)
                    if (point[i][k]<point[j][k])
                        worse_somewhere=true;
                // if point[i] is worse than point[j] at coordinate k then we set worse_somewhere to be true
                
                bool not_better=true; // This variable will be true if p_i is note better than p_j in all coordinate; i.e., for all k, p_i[k]<=p_j[k]
                for (int k=0; k<d; k++)
                    if (point[i][k]>point[j][k])
                        not_better=false;
                // if point[i] is better than point[j], then not_better=true;
                
                // if point[i] is not better than point[j] and point[i] is actually worse in some dimension, then point[i] is not the best
                if (worse_somewhere && not_better) {
                    isBest[i]=false;
                    //cout << i << " is eliminated" << endl; //Debug
                }
            }
        }
    }
    
    // Count the number of interesting points
    int count=0;
    for (int i=0; i<n; i++)
        if (isBest[i])
            count++;

    // This part is used to check the output. It is not necessary
    
    for (int i=0; i<n; i++)
        if (isBest[i]) {
            for (int k=0; k<d; k++)
                cout << point[i][k] << " ";
            cout << endl;
        }

    return count;
}


/************************************************
 * Main 
 ************************************************/


int main () {
    
    int d=0; // d represents the dimension of points.
    int n=0; // n represents the number of points.
    
    vector< vector<float> >  point; // point[i][j] refers to the j-th coordinate of the i-th point
    
    // Variables below are used for measuring the time
    clock_t begin, end; 
    double elapsed_secs; 
    
    /**********************************************
     * Running SimpleAlgo1
     **********************************************/
    
    /* Read input. There are two ways to read an input. See examples below. 
     * You are recommended to read an input again every time you run another algorithm
     */
    
    ReadInput("3.in", n, d, point); // Use this if you want to read from file "x.in"
    // ReadInput(n, d, point); // Use this if you want to key in the input
    
    //cout << "Finishing fetching the input.\n";
    //cout << "Fetched" << n << " points of " << d << " dimensions.\n";
    //cout << "Time is now started." << endl;
    
    begin = clock(); // This line is used 
    
    
    /*************************************
     * Replace your algorithm here 
     *************************************/
    
    // You should check with the solution whether your output is correct.
    cout << "*** SimpleAlgo1 outputs " << SimpleAlgo1(n, d, point) << endl;
 
    
    /**************************************/
    
    // Show how much time the algorithm takes 
    end = clock();
    elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    cout << "Time taken: " << elapsed_secs << " seconds." << endl<<endl;
    
    /**********************************************
     * Running SimpleAlgo2
     * Your code could look as simple as this
     **********************************************/
    
    ReadInput("3.in", n, d, point); // Read input
    //ReadInput(n, d, point);
    begin = clock(); // This line is used to measure the running time
    
    cout << "*** SimpleAlgo2 outputs " << SimpleAlgo2(n, d, point) << endl;
    
    end = clock();
    elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    cout << "Time taken: " << elapsed_secs << " seconds." << endl << endl;
     
	return 0;
}
