import { ReviewInterface } from "./review.interface";

export interface AttractionInterface {
    attraction_id: number ,
    nom: string,
    description: string, 
    difficulte: number,
    visible: boolean,
    reviews: ReviewInterface[] | null
}