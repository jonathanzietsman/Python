import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienInvasion:
    """Main game class that manages all game assets, behavior, and game loop.
    This class handles everything from initializing the game to running the main game loop."""
    
    def __init__(self):
        """Initialize the game and create all necessary game resources.
        This includes setting up the display, game objects, and initial game state."""
        pygame.init()
        
        # Set up the game clock for controlling frame rate
        self.clock = pygame.time.Clock()
        self.settings = Settings() ####
        
        # Create a fullscreen window and store its dimensions
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        
        # Initialize game statistics and scoreboard
        self.stats = GameStats(self) ####
        self.sb = Scoreboard(self) ####
        
        # Create the player's ship and sprite groups for bullets and aliens
        self.ship = Ship(self) ####
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        # Create the initial fleet of aliens
        self._create_fleet()
        
        # Set the background color to a light gray
        self.bg_color = (230, 230, 230)
        
        # Game starts in inactive state until player clicks Play
        self.game_active = False
        
        # Create the Play button
        self.play_button = Button(self, 'Play')
        
    def run_game(self):
        """Main game loop that runs continuously while the game is active.
        Handles all game events, updates, and screen refreshes."""
        while True:
            # Check for player input and game events
            self._check_events()
            
            # Only update game objects if the game is active
            if self.game_active:         
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
        
            # Update the screen and maintain 60 FPS
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        # respond to key presses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        # start new game when the player clicks play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # reset the game settings
            self.settings.initialize_dynamic_settings()
            
            # reset game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active =True
            
            # get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # hide the mouse cursor
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self,event):
        # respond to key presses
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        # respond to key releases
        if event.key == pygame.K_RIGHT:
            # stop the ship from moving to the right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # stop the ship from moving to the left
            self.ship.moving_left = False
    
    def _create_fleet(self):
        # create the fleet of aliens 
        # create an alien an keep adding aliens until theres no room left 
        # space between aliens is on alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 8 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += (2 * alien_width)

            # finised a row, reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height
            
    def _create_alien(self, x_position, y_position):
        # create an alien and place it in the row 
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)    
        
    def _check_fleet_edges(self):
        # respond appropriately if any aliens have reached an edge 
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        # drop the entire fleet and change the fleets direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _fire_bullet(self):
        # create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        # update the position of the bullets and remove any that have disappeared
        # update bullet positions
        self.bullets.update()
        
        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        # respond to bullet-alien collisions
        # remove any bullets and aliens that have colided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # destory existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # increase level
            self.stats.level += 1
            self.sb.prep_level()
        
    def _update_aliens(self):
        # check if fleet is at an edge then update the positions  
        self._check_fleet_edges()
        self.aliens.update()
        
        # look for alien-ship collisons
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        # look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        # respond to ship being hit by an alien
        if self.stats.ships_left > 0:
            # decrement ships left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
        
            # get rid of any remining bullets and aliens 
            self.bullets.empty()
            self.aliens.empty()
        
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        
            # pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        # chekc if any aliens have reached the bottom of the screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # treat this as if the ship got hit
                self._ship_hit()
                break
    
    def _update_screen(self):
        # update images on the screen and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        # draw the score information
        self.sb.show_score()
        
        # draw the play button if the game is active
        if not self.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()
            
if __name__ == '__main__':
    # Create an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            