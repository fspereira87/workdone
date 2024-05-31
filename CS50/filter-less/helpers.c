#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int b = image[i][j].rgbtBlue;
            int g = image[i][j].rgbtGreen;
            int r = image[i][j].rgbtRed;

            int m = round ((b+g+r)/3.0);

            image[i][j].rgbtBlue = m;
            image[i][j].rgbtGreen =m;
            image[i][j].rgbtRed = m;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            int R = image[i][j].rgbtRed;
            int G = image[i][j].rgbtGreen;
            int B = image[i][j].rgbtBlue;


            int sepiaRed = round(0.393*R + 0.769*G + 0.189*B);
            int sepiaGreen = round(0.349*R + 0.686*G + 0.168*B);
            int sepiaBlue = round(0.272*R + 0.534*G + 0.131*B);

            sepiaRed = (sepiaRed>255) ? 255: sepiaRed;
            sepiaGreen = (sepiaGreen>255) ? 255: sepiaGreen;
            sepiaBlue = (sepiaBlue>255) ? 255: sepiaBlue;


            image[i][j].rgbtRed= sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width-j-1];
            image[i][width-j-1] = temp;

        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copyimage[height][width];

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            copyimage[h][w] = image[h][w];
        }
    }

        for (int h = 0; h < height; h++)
        {

            for (int w = 0; w < width; w++)
            {

            int r = 0;
            int g = 0;
            int b = 0;
            int pix = 0;

            for (int i = -1; i<=1; i++)
            {
                for (int j = -1; j<=1; j++)
                {
                    int newH = h+i;
                    int newW = w+j;

                    if (newH >= 0 && newH < height && newW>=0 && newW < width)
                    {


                    pix++;
                    r += copyimage[h+i][w+j].rgbtRed;
                    g += copyimage[h+i][w+j].rgbtGreen;
                    b += copyimage[h+i][w+j].rgbtBlue;
                    }
                }
            }
            image[h][w].rgbtRed = round (r/(float)pix);
            image[h][w].rgbtGreen = round (g/(float)pix);
            image[h][w].rgbtBlue = round (b/(float)pix);
        }

    }
    return;
}

