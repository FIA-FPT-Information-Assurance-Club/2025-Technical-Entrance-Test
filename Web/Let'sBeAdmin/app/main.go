package main

import (
	"encoding/base64"
	"errors"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/gin-gonic/gin"
)

var (
	jwtKey = []byte("MeoBeu8ecb636c")
)

type Claims struct {
	IsAdmin bool `json:"is_admin"`
	jwt.StandardClaims
}

func main() {
	router := gin.Default()

	// Load templates
	router.LoadHTMLGlob("templates/*.html")
	router.Static("/statics", "./statics")
	router.Static("/assets", "./assets")

	// Routes
	router.GET("/", home)
	router.GET("/home", home)
	router.GET("/admin", admin)
	router.POST("/admin", admin)
	router.GET("/robots.txt", robots)
	router.GET("/s3cr3t-p@ssw0rd", s3cr3t)

	// Middleware
	router.Use(errorHandlerMiddleware())

	router.Run(":62233")
}

func home(c *gin.Context) {
	tokenStr, err := c.Cookie("token")
	if err != nil || tokenStr == "" {
		token := createJWT(false)
		c.SetCookie("token", token, int(time.Hour*24), "/", "", false, true)
	}
	base64Xelan := encodeImageToBase64("./statics/xe_lan.png")
	c.HTML(http.StatusOK, "home.html", gin.H{
		"title":  "FIA Entrance",
		"xe_lan": base64Xelan,
	})
}

func admin(c *gin.Context) {
	if c.Request.Method == http.MethodGet {
		tokenStr, err := c.Cookie("token")
		if err != nil || tokenStr == "" {
			c.Redirect(http.StatusFound, "/home")
			return
		}

		claims, err := parseJWT(tokenStr)
		if err != nil || !claims.IsAdmin {
			c.HTML(http.StatusForbidden, "error.html", gin.H{
				"title":        "Access Denied",
				"message":      "You do not have permission to access this page.",
				"redirect_url": "/home",
			})
			return
		}

		base64Meobeo := encodeImageToBase64("./assets/meobeo.jpg")
		c.HTML(http.StatusOK, "admin.html", gin.H{
			"title":        "Admin Page",
			"redirect_url": "/home",
			"Meobeo":       base64Meobeo,
		})
	} else if c.Request.Method == http.MethodPost {
		var requestBody struct {
			User string `json:"hacker" binding:"required"`
		}

		if err := c.ShouldBindJSON(&requestBody); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{
				"error": "Invalid request data",
			})
			return
		}

		if requestBody.User == "MeoBeuIsHere" {
			c.String(http.StatusOK, "FIA{you_cracked_jwt_and_captured_the_request}")
			return
		}

		c.JSON(http.StatusUnauthorized, gin.H{
			"error": "Unauthorized",
		})
		return
	}
}

func robots(c *gin.Context) {
	content, err := os.ReadFile("robots.txt")
	if err != nil {
		c.String(http.StatusInternalServerError, "Error reading robots.txt file: %v", err)
		return
	}
	c.Data(http.StatusOK, "text/plain; charset=utf-8", content)
}

func s3cr3t(c *gin.Context) {
	passwordList, err := os.ReadFile("passwords.txt")
	if err != nil {
		c.String(http.StatusInternalServerError, "Error reading passwords.txt file: %v", err)
		return
	}
	c.Data(http.StatusOK, "text/plain; charset=utf-8", passwordList)
}

func createJWT(isAdmin bool) string {
	claims := Claims{
		IsAdmin: isAdmin,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: time.Now().Add(time.Hour * 24).Unix(),
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenStr, _ := token.SignedString(jwtKey)
	return tokenStr
}

func parseJWT(tokenStr string) (*Claims, error) {
	claims := &Claims{}
	token, err := jwt.ParseWithClaims(tokenStr, claims, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, errors.New("unexpected signing method")
		}
		return jwtKey, nil
	})
	if err != nil || !token.Valid {
		return nil, err
	}
	return claims, nil
}

func errorHandlerMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Next()
		if len(c.Errors) > 0 {
			c.HTML(http.StatusInternalServerError, "error.html", gin.H{
				"title":        "Error",
				"message":      "Something went wrong. Please try again later.",
				"redirect_url": "/",
			})
		}
	}
}

func encodeImageToBase64(path string) string {
	imageData, err := os.ReadFile(path)
	if err != nil {
		log.Printf("Error reading image file: %v", err)
		return ""
	}

	return base64.StdEncoding.EncodeToString(imageData)
}
