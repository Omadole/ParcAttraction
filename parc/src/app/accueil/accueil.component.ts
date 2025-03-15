import { Component } from '@angular/core';
import { AttractionService } from '../Service/attraction.service';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { AttractionInterface } from '../Interface/attraction.interface';
import { MatCardModule } from '@angular/material/card';
import { ReviewInterface } from '../Interface/review.interface';

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [CommonModule, MatCardModule],
  templateUrl: './accueil.component.html',
  styleUrl: './accueil.component.scss'
})
export class AccueilComponent {

  constructor(public attractionService: AttractionService)
  {
  }
  
  public attractions: Observable<AttractionInterface[]> = this.attractionService.getVisibleAttraction()

  showReviews: boolean[] = [];

  ngOnInit() {
    // Initialiser l'état d'affichage des critiques pour chaque attraction
    this.attractions.subscribe(data => {
        this.showReviews = new Array(data.length).fill(false);
    });
  }

  toggleReviews(index: number) {
    this.showReviews[index] = !this.showReviews[index];
  }

}
