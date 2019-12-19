import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { getBodyNode } from '@angular/animations/browser/src/render/shared';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-guess-input',
  templateUrl: './guess-input.component.html',
  styleUrls: ['./guess-input.component.scss']
})
export class GuessInputComponent implements OnInit {

  stockForm = new FormGroup({
    symbolControl: new FormControl('', [
      Validators.required
    ]),
    guessControl:  new FormControl('', [
      Validators.required
    ]),
  });

  httpOptions = {
    headers: new HttpHeaders({
      'Access-Control-Allow-Origin': '*'
    }),
    observe: 'response' as 'response'
  };

  serverUrl = 'http://exam.decg.io:8080/';

  resStr = '';

  constructor(private http: HttpClient, private dialog: MatDialog) { }

  ngOnInit() {
  }

  onSubmit() {
    this.resStr = '';
    if (!this.stockForm.get('symbolControl').hasError('required') &&
        !this.stockForm.get('guessControl').hasError('required')) {
      const symbol = this.stockForm.get('symbolControl').value;
      const guess = this.stockForm.get('guessControl').value;
      this.http.get(this.serverUrl + `guess/${symbol}/${guess}`, this.httpOptions)
      .subscribe(response => {
        console.log(response);
        this.resStr = (response.body as any).message;
      });
    }
  }
}
