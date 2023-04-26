<?php
    session_start();

    $name = $_POST['name'] ?? $_SESSION['name'];
    $_SESSION['name'] = $name;

    $correct_answers = ['b4s364_s3cr3tfl4g', '179.60.146.16', '172.31.44.101', 'h0k1ngisc0m1ng', 'r4ns0mw4r3'];
    $user_answers = $_POST['user_answers'] ?? [];
    $score = 0;
    $submitted = isset($_POST['submit']);

    if ($submitted) {
        for ($i = 0; $i < count($correct_answers); $i++) {
            if (in_array(strtolower($user_answers[$i]), $correct_answers)) {
                $score += 10;
            }
        }
        session_destroy();
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRPYA - Challenges</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <?php if (!$submitted): ?>
        <h1>Hello, <?= htmlspecialchars($name) ?>! Welcome to CRPYA Challenges!</h1>
        <form action="challenges.php" method="POST">
            <?php for ($i = 1; $i <= 5; $i++): ?>
                <label for="user_answers[<?= $i - 1 ?>]">Challenge <?= $i ?>:</label>
                <input type="password" id="user_answers[<?= $i - 1 ?>]" name="user_answers[]" required>
                <br>
            <?php endfor; ?>

            <button type="submit" name="submit">Submit your Response</button>
        </form>
    <?php else: ?>
        <h1>CRPYA Certified</h1>
        <p>Congratulations, <?= htmlspecialchars($name) ?>! You've completed the PyWars challenges.</p>
        <p>Your Score: <?= $score ?> of <?= count($correct_answers) * 10 ?> Score.</p>
 	<img src="crpya.png" alt="Certificado PyWars">
    <?php endif; ?>
</body>
</html>
