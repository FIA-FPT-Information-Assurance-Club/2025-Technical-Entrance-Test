const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");

const app = express();
const PORT = 8386;

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(cookieParser());

app.use((req, res, next) => {
  res.setHeader("X-Flag-Part2", "c4lm_4nd_");

  if (!req.cookies.user) res.cookie("user", "guest", { httpOnly: true });
  next();
});

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.render("index", {
    title: "Avenger Assemble",
    typedText: "Welcome to the Avenger!"
  });
});

app.get("/hidden_admin_panel", (req, res) => {
  if (!req.cookies.flag_part3) {
    res.cookie("flag_part3", "1n5p3c7_", { httpOnly: true });
  }
  const user = req.cookies.user || "guest";
  if (user === "admin") {
    const flag = "50urc3_";
    res.render("admin", { flag });
  } else {
    res.status(403).render("access_denied");
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
